from django.utils import timezone
from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.vendor.update_metrics()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.vendor.update_metrics()