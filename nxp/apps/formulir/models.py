from django.db import models


class Formulir(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    reward_number = models.CharField(max_length=100, blank=True, null=True)
    job = models.TextField(max_length=50, blank=True, null=True)
    oil_type = models.TextField(max_length=254, blank=True, null=True)
    TYPE = (
        ('gopay', 'Gopay'),
        ('ovo', 'OVO'),
        ('dana', 'Dana'),
        ('shopee_pay', 'ShopeePay'),
    )
    wallet_type = models.TextField(max_length=254, CBOICES=TYPE)


    def __str__(self):
        return self.name
