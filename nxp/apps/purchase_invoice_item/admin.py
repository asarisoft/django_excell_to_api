
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PurchaseInvoiceItem
from import_export import resources


class PurchaseInvoiceItemResources(resources.ModelResource):
    class Meta:
        model = PurchaseInvoiceItem
        exclude = ('id')
        import_id_fields = (
            'no_pemasok',
            'date',
            'nama_pemasok',
            'no_purchase_invoice',
            'no_faktur_vendor',
            'keterangan',
            'no_akun_persediaan_barang',
            'nama_akun_persediaan_barang',
            'jumlah',
            'id_barang',
            'no_barang',
            'keterangan_barang',
            'qty',
            'unit'
        )


@admin.register(PurchaseInvoiceItem)
class PurchaseInvoiceItemAdmin(ImportExportModelAdmin):
    list_display = ["no_purchase_invoice", "nama_pemasok"]
    search_fields = ["no_purchase_invoice", "nama_pemasok"]
    resource_class = PurchaseInvoiceItemResources
    pass
