from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import JV
from import_export import resources

class JVResources(resources.ModelResource):
    class Meta:
        model = JV
    # fields = ("id", "tgl_jv","no_akun","nama_akun","catatan","nilai_asing","nama_dep","nama_proyek","no_jv","bank_code","nama_bank")
       
        
@admin.register(JV)
class JVAdmin(ImportExportModelAdmin):
    list_display=["no_jv","no_akun","tgl_jv","nama_akun"]
    pass
