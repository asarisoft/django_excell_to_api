from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import Group

admin.site.site_header = "Import Excell Admin"
admin.site.site_title = "Import Excell Admin"
admin.site.index_title = "Welcome to Import Excell Admin"
admin.site.unregister(Group)

urlpatterns = [
    path('', admin.site.urls),
    # path('', include('nxp.backoffice.urls', namespace='backoffice')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# di server saat settings debug true
if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
