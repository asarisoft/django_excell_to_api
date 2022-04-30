
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceItem
from import_export import resources

        
@admin.register(PurchaseInvoiceItem)
class PurchaseInvoiceItemAdmin(ImportExportModelAdmin):
    list_display=["no_pemasok","nama_pemasok"]
    pass
