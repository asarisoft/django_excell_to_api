from django.db import models



class SerialNumber(models.Model):
    serial_number = models.CharField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS = (
        ('new', 'new'),
        ('redeem', 'redeem'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='new')
    TYPE = (
        ('U', 'U'), #user
        ('D', 'D'), #dealer
    )
    type = models.CharField(max_length=10, choices=STATUS, default='new')
    order = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.serial_number
