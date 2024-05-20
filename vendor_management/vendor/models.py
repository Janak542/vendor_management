from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def _str_(self):
        return self.name
    
    def update_metrics(self):
        orders = PurchaseOrder.objects.filter(vendor=self, status='completed')
        total_orders = orders.count()

        if total_orders == 0:
            return

        on_time_deliveries = orders.filter(delivery_date__lte=models.F('delivery_date')).count()
        self.on_time_delivery_rate = (on_time_deliveries / total_orders) * 100

        self.quality_rating_avg = orders.aggregate(avg=models.Avg('quality_rating'))['avg'] or 0

        response_times = orders.exclude(acknowledgment_date__isnull=True).annotate(
            response_time=models.ExpressionWrapper(models.F('acknowledgment_date') - models.F('issue_date'), output_field=models.DurationField())
        )
        self.average_response_time = response_times.aggregate(avg=models.Avg('response_time'))['avg'].total_seconds() or 0

        successful_fulfillments = orders.filter(quality_rating__gte=0).count()
        self.fulfillment_rate = (successful_fulfillments / total_orders) * 100

        self.save()

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()