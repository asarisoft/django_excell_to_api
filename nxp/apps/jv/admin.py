from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import JV
from import_export import resources

        
@admin.register(JV)
class JVAdmin(ImportExportModelAdmin):
    list_display=["no_jv","no_akun","tgl_jv","nama_akun"]
    pass
