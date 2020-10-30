from django.contrib import admin

from .models import *

class MenuAdmin(admin.ModelAdmin):    
    list_display = ('name', 'one_page_url', 'order', 'is_active')

admin.site.register(Menu, MenuAdmin)
