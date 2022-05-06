from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Invoice
from import_export import resources


class InvoiceResources(resources.ModelResource):
    class Meta:
        model = Invoice
        exclude = ('id')
        import_id_fields = ('no_faktur','tgl_faktur','no_barang', 'id_barang')
        # fields = ("id", "tgl_jv","no_akun","nama_akun","catatan","nilai_asing","nama_dep","nama_proyek","no_jv","bank_code","nama_bank")
       
        
@admin.register(Invoice)
class InvoiceAdmin(ImportExportModelAdmin):
    list_display=["tgl_faktur","no_pelanggan","id_pelanggan","nama_pelanggan"]
    resource_class = InvoiceResources
    pass
