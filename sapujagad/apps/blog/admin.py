from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class BlogAdmin(SummernoteModelAdmin):    
    summernote_fields = '__all__'
    list_display = ('title', 'preview')

admin.site.register(Blog, BlogAdmin)

