from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "NXP Admin"
admin.site.site_title = "NXP Admin Portal"
admin.site.index_title = "Welcome to NXP Admin Portal"

urlpatterns = [
    path('', include('nxp.frontend.urls', namespace='frontend')),
    path('nxp-admin/', admin.site.urls),
    path('backoffice/', include('nxp.backoffice.urls', namespace='backoffice')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# di server saat settings debug true
if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
