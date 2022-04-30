
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurhaseInvoiceExpense
from import_export import resources

        
@admin.register(PurhaseInvoiceExpense)
class PurhaseInvoiceExpenseAdmin(ImportExportModelAdmin):
    list_display=["tgl_faktur","no_purchase_invoice"]
    pass
