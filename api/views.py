import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import InvoiceItems, BillSundry, Header
from api.validators import Validators

# @csrf_exempt
# def login(request):
#     body = request.body or '{}'
#     body_json = json.loads(body)
#     username = body_json.get("username")
#     password = body_json.get("password")
#     if not username or not password:
#         return JsonResponse({"status": 0, "message": "Please enter valid credentials"}, status=403)
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return JsonResponse({"status": 0, "message": "Logged in successfully", "data": {"user": user}}, status=200)
#     return JsonResponse({"status": 0, "message": "Unable to login", "data": {"user": user}}, status=400)

# def logout(request):
#     logout(request)

# @login_required(login_url="/api/login")

# Create a CRUD endpoint for an invoice. It must follow the following rules:
# Build 5 endpoints, create, update, delete, retrieve & list. Follow the REST principles.
# Each endpoint must accept the entire Invoice in one JSON during CRUD operation. That is, Each Invoice can have many InvoiceItems and InvoiceBillSundrys.
# Validations for InvoiceItems:
# Amount = Quantity x Price
# Price, Quantity, and Amount must be greater than zero.
# Validations for BillSundrys:
# The amount can be negative or positive.
# Validations for Invoice:
# TotalAmount = Sum(InvoiceItems’s Amount) + Sum(InvoiceBillSundry’s Amount)
# InvoiceNumber should autoincremental and hence should be unique.
# Raise appropriate error messages if any validation fails.


def index(request):
    return JsonResponse({"status": 1, "message": "Success"})

def create(request):
    body = request.body
    body_json = json.loads(body)
    items = body_json.get('items')
    for item in items:
        if not Validators.validate_invoice_item(item):
            raise 'Error in creating invoice item'
        InvoiceItems.objects.create(**item)
    bill_sundrys = body_json.get('bill_sundrys')
    for row in bill_sundrys:
        if not Validators.validate_bill_sundry(row):
            raise ('Error in creating bill sundry')
        BillSundry.objects.create(**row)
    del body_json['items']
    del body_json['bill_sundrys']
    Header.objects.create(**body_json)
    return JsonResponse({"message": "created"}, status=201)

def update(request):
    body = request.body
    body_json = json.loads(body)
    items = body_json.get('items')
    for item in items:
        item_update = item
        del item_update['id']
        InvoiceItems.objects.filter(id=item.get('id')).update(**item_update)
    bill_sundrys = body_json.get('bill_sundrys')
    for row in bill_sundrys:
        bill_sundry = row
        del bill_sundrys['id']
        BillSundry.objects.filter(id=row.get('id')).update(**bill_sundry)
    return JsonResponse({"message": "updated"}, status=200)
    
