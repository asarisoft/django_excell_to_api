from django.contrib import admin

from .models import *


class SettingsModelAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    ordering = ('name',)
    list_display = ('name', 'text_value', 'img_value')

admin.site.register(Settings, SettingsModelAdmin)