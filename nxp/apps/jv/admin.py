from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import JV
from import_export import resources


class JVResources(resources.ModelResource):
    class Meta:
        model = JV
        exclude = ('id')
        import_id_fields = ('no_jv', 'no_akun', 'tgl_jv',
                            'keterangan', 'debit', 'kredit', 'nama_dep')


@admin.register(JV)
class JVAdmin(ImportExportModelAdmin):
    list_display = ["no_jv", "no_akun", "tgl_jv", "nama_akun", "debit", "kredit", "description]
    search_fields = ["no_jv", "no_akun", "tgl_jv", "nama_akun", "debit", "kredit", "description"]
    resource_class = JVResources
    pass
