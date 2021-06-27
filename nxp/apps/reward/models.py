from django.db import models


class Scan(models.Model):
    dealer_code = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.ForeignKey('serial_number.SerialNumber', on_delete=models.CASCADE)
    product = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % self.serial_number

    def save(self, *args, **kwargs):
        super(Scan, self).save(*args, **kwargs)
        Balance.objects.update_or_create(
            scan=self, 
            user=self.user,
            defaults={
                "credit": self.serial_number.value,  
                "type": "credit"
            }
        )


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
    value = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.user

    def save(self, *args, **kwargs):
        super(Redeem, self).save(*args, **kwargs)
        if self.status == 'paid':
            Balance.objects.update_or_create(
                redeem=self, 
                user=self.user,
                defaults={
                    "debit": self.value,  
                    "type":'debit'
                }
            )


class Balance(models.Model):
    datetime = models.DateField(auto_now_add=True)
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

    def __unicode__(self):
        return "%s" % self.user
    
    def save(self, *args, **kwargs):
        last_balance = Balance.objects.filter(user=self.user).order_by('-id').first()
        last_balance = last_balance.balance if last_balance else 0
        if self.type == 'credit':
            print("sdfsdfsdfsdfsdfsdfsdfdsfsdfsdfsdfsd")
            self.balance = last_balance + self.credit
        else:
            self.balance = last_balance - self.debit
        
        print(self.balance)
        super(Balance, self).save(*args, **kwargs)

        
