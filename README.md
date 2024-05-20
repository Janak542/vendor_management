# Vendor Management System

## Setup Instructions
1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Apply migrations: python manage.py migrate
4. Run the server: python manage.py runserver

## API Endpoints
- POST /api/vendors/: Create a new vendor
- GET /api/vendors/: List all vendors
- GET /api/vendors/{vendor_id}/: Retrieve vendor details
- PUT /api/vendors/{vendor_id}/: Update vendor details
- DELETE /api/vendors/{vendor_id}/: Delete vendor
- POST /api/purchase_orders/: Create a purchase order
- GET /api/purchase_orders/: List all purchase orders
- GET /api/purchase_orders/{po_id}/: Retrieve purchase order details
- PUT /api/purchase_orders/{po_id}/: Update purchase order
- DELETE /api/purchase_orders/{po_id}/: Delete purchase order
- GET /api/vendors/{vendor_id}/performance: Retrieve vendor performance metrics

## Running Tests
Run the tests with:
```bash
python manage.py test
