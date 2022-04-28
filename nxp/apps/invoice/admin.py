from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Invoice
from import_export import resources

        
@admin.register(Invoice)
class InvoiceAdmin(ImportExportModelAdmin):
    list_display=["tgl_faktur","no_pelanggan","id_pelanggan","nama_pelanggan"]
    pass
