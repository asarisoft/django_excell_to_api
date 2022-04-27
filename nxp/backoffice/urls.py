from django.urls import path, include
from .views import (
    login_view, log_out, index, 
    cashflow, json_data, 
    generate_json_data,
    process_data
)

app_name = "backoffice"
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('log_out/', log_out, name='log_out'),
    # path('rewards/', include('nxp.backoffice.rewards.urls', namespace='rewards')),
    # path('users/', include('nxp.backoffice.users.urls', namespace='users')),

    # new
    # path('upload_data/', upload_data, name='upload_data'),
    path('cashflow/', cashflow, name='cashflow'),
    path('generate-json-data/', generate_json_data, name='generate_json_data'),
    path('json_data/', json_data, name='json_data'),
    path('process-data/', process_data, name='process_data'),
]
