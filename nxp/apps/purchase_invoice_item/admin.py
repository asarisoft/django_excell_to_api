
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceItem
from import_export import resources


class PurchaseInvoiceItemResources(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceItem
        exclude = ('id')
        import_id_fields = ('no_purchase_invoice','no_barang','no_akun_persediaan_barang','jumlah')
        
        
@admin.register(PurchaseInvoiceItem)
class PurchaseInvoiceItemAdmin(ImportExportModelAdmin):
    list_display=["no_purchase_invoice","nama_pemasok"]
    resource_class = PurchaseInvoiceItemResources
    pass


       
        