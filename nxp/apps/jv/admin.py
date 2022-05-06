from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import JV
from import_export import resources

class JVResources(resources.ModelResource):
    class Meta:
        model = JV
        exclude = ('id')
        import_id_fields = ('no_jv','no_akun','keterangan', 'debit', 'kredit')
       
        
@admin.register(JV)
class JVAdmin(ImportExportModelAdmin):
    list_display=["no_jv","no_akun","tgl_jv","nama_akun"]
    resource_class = JVResources
    pass


