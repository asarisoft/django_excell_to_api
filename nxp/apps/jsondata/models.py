from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class JSONData(models.Model)
    key = models.CharField(max_length=100, choices=TYPE, unique=True)
    TYPE = (
        ('purchase_invoice_item', 'Purchase Invoice Item'),
        ('purchase_invoice_expense', 'Purchase Invoce Expense'),
        ('cash_flow', 'Cash Flow'),
        ('jv', 'JV'),
        ('sales', 'Sales'),
    )
    type_name = models.CharField(max_length=100, choices=TYPE, unique=True)
    json_data  = models.TextField(blank=True, null=True) #a
    item_joined  = models.IntegerField(default=1, blank=True, null=True) #a
    response  = models.TextField(blank=True, null=True) #a
    STATUS = (
        ('new', 'New'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )
    type_name = models.CharField(max_length=100, choices=STATUS, unique=True)
