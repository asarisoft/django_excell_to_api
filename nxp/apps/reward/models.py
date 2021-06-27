from django.db import models
from django.utils import timezone
from .models import *


class Scan(models.Model):
    dealer_code = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.ForeignKey('serial_number.SerialNumber', on_delete=models.CASCADE)
    product = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % self.serial_number

    
    def serialize(self):
        return  {
            "id" : self.id,
            "dealer_code" : self.dealer_code,
            "serial_number" : self.serial_number.serial_number,
            "value" : f'{self.serial_number.value:,}'.replace(',','.'),
            "product" : self.product,
            "user" : self.user.name
        }


    def save(self, *args, **kwargs):
        super(Scan, self).save(*args, **kwargs)
        Balance.objects.update_or_create(
            scan=self, 
            user=self.user,
            defaults={
                "credit": self.serial_number.value,  
                "type": "credit",
                "status": "success"
            }
        )


class Redeem(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
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
    )
    status = models.CharField(max_length=10, choices=STATUS, default='new')
    value = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.user
    
    def serialize(self):
        return  {
            "id" : self.id,
            "datetime" : self.datetime.strftime("%d-%m-%Y (%H:%M)"),
            "user" : self.user.name,
            "wallet_type" : self.get_wallet_type_display(),
            "value" : f'{self.value:,}'.replace(',','.'),
            "status" : self.get_status_display()
        }

    def save(self, *args, **kwargs):
        super(Redeem, self).save(*args, **kwargs)
        Balance.objects.update_or_create(
            redeem=self, 
            user=self.user,
            defaults={
                "debit": self.value,  
                "type": 'debit',
                "status": 'success' if self.status == 'paid' else 'pending',
            }
        )


class Balance(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    TYPE = (
        ('debit', 'Debit'), #diambil
        ('credit', 'Credit'), #bertambah
    )
    type = models.CharField(null=True, choices=TYPE, max_length=10)
    redeem = models.OneToOneField("reward.Redeem", null=True, unique=True, on_delete=models.CASCADE)
    scan = models.OneToOneField("reward.Scan", null=True, unique=True, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)
    debit = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    STATUS = (
        ('pending', 'Pending'), #diambil
        ('success', 'Sukses'), #bertambah
    )
    status = models.CharField(null=True, choices=STATUS, max_length=10, default="pending")
    
    def __unicode__(self):
        return "%s" % self.user

    def serialize(self):

        info = {}
        if self.redeem:
            info = self.redeem.serialize()
        elif self.scan:
            info = self.scan.serialize()
            
        return  {
            "user" : self.datetime,
            "type" : self.type,
            "credit" : f'{self.credit:,}'.replace(',','.'),
            "debit" : f'{self.debit:,}'.replace(',','.'),
            "balance" : f'{self.balance:,}'.replace(',','.'),
            "user" : self.user.name,
            "status" : self.get_status_display(),
            "info": info,
        }
    
    def save(self, *args, **kwargs):
        last_balance = Balance.objects.filter(user=self.user).order_by('-id').first()
        last_balance = last_balance.balance if last_balance else 0
        if self.type == 'credit':
            self.balance = last_balance + self.credit
        else:
            self.balance = last_balance - self.debit
        
        super(Balance, self).save(*args, **kwargs)
