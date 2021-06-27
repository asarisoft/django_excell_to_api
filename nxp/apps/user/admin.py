from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

# from import_export.admin import ImportExportModelAdmin

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (
            'username', 'password', 'name', 'mobile_number',
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        # ('Important dates', {'fields': ('registered_date',)}),
    )

    list_display = ('username',  'name', 'mobile_number')
    # # list_filter = ('is_staff', 'is_superuser', 'is_active',)
    # search_fields = ('mobile_number', 'username', 'name', 'email',
    #                  'kelurahan__name', 'kecamatan__name', 'tps__name','nik')
    # ordering = ('mobile_number', 'username',)
    # autocomplete_fields = ('kelurahan', 'kecamatan',
    #                        'kabupaten_kota', 'registered_by', 'tps')
    # list_filter = (
    #     ('is_staff', DropdownFilter),
    #     ('is_superuser', DropdownFilter),
    #     ('province', RelatedDropdownFilter),
    #     ('kabupaten_kota', RelatedDropdownFilter),
    # )
    
admin.site.register(User, UserAdmin)
