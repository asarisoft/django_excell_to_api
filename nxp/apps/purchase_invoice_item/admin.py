
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceItem
from import_export import resources


class PurchaseInvoiceItemResources(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceItem
        # fields = ("id", "tgl_jv","no_akun","nama_akun","catatan","nilai_asing","nama_dep","nama_proyek","no_jv","bank_code","nama_bank")
       
        
@admin.register(PurchaseInvoiceItem)
class PurchaseInvoiceItemAdmin(ImportExportModelAdmin):
    list_display=["no_purchase_invoice","nama_pemasok"]
    pass
