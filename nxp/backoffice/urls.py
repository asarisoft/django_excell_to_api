from django.urls import path, include
from .views import (
    login_view, log_out, index, 
    generate_json_data,
    process_data,
    json_data, 
    json_data_detail,

    purchase_invoice_item,
    purchase_invoice_expense,
    cashflow, 
    jv,
    invoice,
    download_file
)

app_name = "backoffice"
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('log_out/', log_out, name='log_out'),

    path('purchase-invoice-item/', purchase_invoice_item, name='purchase_invoice_item'),
    path('purchase-invoice-expense/', purchase_invoice_expense, name='purchase_invoice_expense'),
    path('cashflow/', cashflow, name='cashflow'),
    path('jv/', jv, name='jv'),
    path('invoice/', invoice, name='invoice'),

    path('generate-json-data/', generate_json_data, name='generate_json_data'),
    path('json-data/', json_data, name='json_data'),
    path('<int:id>/json-data-detail/', json_data_detail, name='json_data_detail'),
    path('process-data/', process_data, name='process_data'),
    path('download/<str:filename>', download_file, name="download_file"),
]

