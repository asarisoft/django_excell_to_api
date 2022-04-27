from django.contrib import admin

from .models import *

        
@admin.register(JSONData)
class JSONDataAdmin(admin.ModelAdmin):
    list_display=["key","model","item_joined",]
    list_filter=["model"]
    # resource_class = CashflowResource
    # change_list_template = "admin/cashflow_list.html"
    pass