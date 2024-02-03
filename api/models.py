from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
# Create an Invoice CRUD Endpoints. The structure of tables in the application is as follows:
# Invoice Header
# Id: UUID
# Date: string (UTC)
# InvoiceNumber: number
# CustomerName: string
# BillingAddress: string
# ShippingAddress: string
# GSTIN: string
# TotalAmount: Decimal

# Invoice Items
# Id: UUID
# itemName: string
# Quantity: decimal
# Price: decimal
# Amount: decimal

# Invoice BillSundry
# Id: UUID
# billSundryName: string
# Amount: decimal
import uuid

class Header(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateTimeField()
    invoce_num = models.IntegerField(blank=False)
    customer_name = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    gstin = models.CharField(max_length=255)
    total_amount = models.FloatField()


class InvoiceItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    item_name = models.CharField(max_length=200) 
    quantity = models.FloatField()
    price = models.FloatField()
    amount = models.FloatField()
    # header = models.ForeignKey

class BillSundry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    bill_sundry_name = models.CharField(max_length=200)
    amount = models.FloatField()


