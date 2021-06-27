from django.urls import path
from .views import *

app_name = "frontend"
urlpatterns = [
    path('', scan, name='scan'),
    # path('', authenticated_scan, name='authenticated_scan'),
    path('redeem/', redeem, name='redeem'),
    path('api-scan/', api_scan, name='api_scan'),
    path('api-get-info/', get_information, name='get_information'),
    path('api-redeem/', api_redeem, name='api_redeem'),
]
