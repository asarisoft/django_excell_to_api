from django.db import models
from django.utils import timezone
from .models import *
from datetime import datetime, timedelta


class JSONData(models.Model):
    key = models.CharField(max_length=100)
    TYPE = (
        ('purchaseinvoice', 'purchaseinvoice'),
        ('cashflow', 'cashflow'),
        ('jv', 'jv'),
        ('invoice', 'invoice'),
    )
    type = models.CharField(max_length=100, choices=TYPE, null=True)
    MODEL = (
        ('purchaseinvoiceitem', 'purchaseinvoiceitem'),
        ('purchaseinvoiceexpense', 'purchaseinvoiceexpense'),
        ('cashflow', 'cashflow'),
        ('jv', 'jv'),
        ('invoice', 'invoice'),
    )
    model = models.CharField(max_length=100, choices=TYPE, null=True)
    json_data  = models.TextField(blank=True, null=True) #a
    item_joined  = models.IntegerField(default=1, blank=True, null=True) #a
    response  = models.TextField(blank=True, null=True) #a
    STATUS = (
        ('new', 'new'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )
    status = models.CharField(max_length=100, choices=STATUS, default="new")

    def __str__(self):
        return f"{self.key} {self.model}"

    class Meta:
        unique_together = ('key', 'model', 'type')
