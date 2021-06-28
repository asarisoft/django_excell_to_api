from django.contrib import admin

from .models import *

class RedeemAdmin(admin.ModelAdmin):
    search_fields = ['user__mobile_number', 'user__name']

admin.site.register(Scan)
admin.site.register(Redeem)
admin.site.register(Balance)