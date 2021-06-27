from django.db import models


class Scan(models.Model):
    dealer_code = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.serial_number

    
class Redeem(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    nominal = models.IntegerField(default=0)
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

        
