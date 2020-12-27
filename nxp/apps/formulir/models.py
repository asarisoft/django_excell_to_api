from django.db import models


class Formulir(models.Model):
    dealer_code = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    oil_type = models.TextField(max_length=50, blank=True, null=True)
    TYPE = (
        ('gopay', 'Gopay'),
        ('ovo', 'OVO'),
        ('dana', 'Dana'),
        ('shopee_pay', 'ShopeePay'),
    )
    wallet_type = models.CharField(max_length=10, choices=TYPE)
    STATUS = (
        ('new', 'Baru'),
        ('paid', 'Dibayar'),
        ('cancelled', 'Di Cancel'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='new')


    def __str__(self):
        return self.name
