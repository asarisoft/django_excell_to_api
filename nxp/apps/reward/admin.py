from django.contrib import admin

from .models import *

admin.site.register(Scan)
admin.site.register(Redeem)
admin.site.register(Balance)