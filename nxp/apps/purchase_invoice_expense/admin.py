
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceExpense
from import_export import resources

class PurchaseInvoiceExpenseResources(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceExpense
        # fields = ("id", "tgl_jv","no_akun","nama_akun","catatan","nilai_asing","nama_dep","nama_proyek","no_jv","bank_code","nama_bank")
       
        

@admin.register(PurchaseInvoiceExpense)
class PurchaseInvoiceExpenseAdmin(ImportExportModelAdmin):
    list_display=["tgl_faktur","no_purchase_invoice"]
    pass
