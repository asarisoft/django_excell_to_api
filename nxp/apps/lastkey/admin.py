from django.contrib import admin

from .models import *

        
@admin.register(LastKey)
class LastKeyAdmin(admin.ModelAdmin):
    list_display=["last_key"]
    # resource_class = CashflowResource
    # change_list_template = "admin/cashflow_list.html"
    pass