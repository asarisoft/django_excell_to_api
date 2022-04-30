from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Cashflow
from import_export import resources

class CashflowResource(resources.ModelResource):
    class Meta:
        model = Cashflow
        # fields = ("id", "tgl_jv","no_akun","nama_akun","catatan","nilai_asing","nama_dep","nama_proyek","no_jv","bank_code","nama_bank")
        
@admin.register(Cashflow)
class CashflowAdmin(ImportExportModelAdmin):
    list_display=["tgl_jv","no_akun","nama_akun","catatan","nilai_asing","nama_dep","nama_proyek","no_jv","bank_code","nama_bank"]
    # resource_class = CashflowResource
    # change_list_template = "admin/cashflow_list.html"
    pass
