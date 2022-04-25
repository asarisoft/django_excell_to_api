from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class JSONData(models.Model):
    key = models.CharField(max_length=100)
    TYPE = (
        ('PurchaseItem', 'PurchaseItem'),
        ('PurchaseExpense', 'PurchaseExpense'),
        ('Cashflow', 'Cashflow'),
        ('JV', 'JV'),
        ('Sales', 'Sales'),
    )
    model = models.CharField(max_length=100, choices=TYPE, null=True)
    json_data  = models.TextField(blank=True, null=True) #a
    item_joined  = models.IntegerField(default=1, blank=True, null=True) #a
    response  = models.TextField(blank=True, null=True) #a
    STATUS = (
        ('new', 'New'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )
    status = models.CharField(max_length=100, choices=STATUS, default="new")

    class Meta:
        unique_together = ('key', 'model',)
