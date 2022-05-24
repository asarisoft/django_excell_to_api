
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceExpense
from import_export import resources


class PurchaseInvoiceExpenseResources(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceExpense
        exclude = ('id')
        import_id_fields = (
            'tgl_faktur',
            'no_purchase_invoice',
            'vendor_code',
            'nama_pemasok',
            'no_faktur_vendor',
            'keterangan',
            'no_akun_beban',
            'nama_akun_beban',
            'nilai_beban',
            'item_id',
            'item_name',
            'qty',
            'unit',
        )


@admin.register(PurchaseInvoiceExpense)
class PurchaseInvoiceExpenseAdmin(ImportExportModelAdmin):
    list_display = ["no_purchase_invoice"]
    resource_class = PurchaseInvoiceExpenseResources
    pass
