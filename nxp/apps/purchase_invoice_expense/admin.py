
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceExpense
from import_export import resources

class PurchaseInvoiceExpenseResources(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceExpense
        exclude = ('id')
        import_id_fields = ('no_purchase_invoice','item_id','item_name','qty', 'nilai_beban', 'no_akun_beban')
       
        

@admin.register(PurchaseInvoiceExpense)
class PurchaseInvoiceExpenseAdmin(ImportExportModelAdmin):
    list_display=["no_purchase_invoice"]
    resource_class = PurchaseInvoiceExpenseResources
    pass
