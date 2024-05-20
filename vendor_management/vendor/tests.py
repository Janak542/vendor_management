from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Vendor, PurchaseOrder

class VendorTests(APITestCase):
    def test_create_vendor(self):
        url = reverse('vendor-list')
        data = {
            'name': 'Test Vendor',
            'contact_details': 'Contact details',
            'address': 'Address',
            'vendor_code': 'V12345'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PurchaseOrderTests(APITestCase):
    def test_create_purchase_order(self):
        vendor = Vendor.objects.create(name='Test Vendor', contact_details='Contact details', address='Address', vendor_code='V12345')
        url = reverse('purchaseorder-list')
        data = {
            'po_number': 'PO12345',
            'vendor': vendor.id,
            'order_date': '2024-05-19T12:00:00Z',
            'delivery_date': '2024-05-20T12:00:00Z',
            'items': {},
            'quantity': 10,
            'status': 'pending',
            'issue_date': '2024-05-19T12:00:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)