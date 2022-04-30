from django.urls import path, include
from .views import (
    login_view, log_out, index, 
    cashflow, json_data, 
    generate_json_data,
    process_data,
    purchase_invoice_item,
    purchase_invoice_expense
)

app_name = "backoffice"
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('log_out/', log_out, name='log_out'),

    path('purchase-invoice-item/', purchase_invoice_item, name='purchase_invoice_item'),
    path('purchase-invoice-expense/', purchase_invoice_expense, name='purchase_invoice_expense'),
    path('cashflow/', cashflow, name='cashflow'),
    # path('purchase-invoice-item/', purchase_invoice_item, name='jv'),
    # path('purchase-invoice-item/', purchase_invoice_item, name='invoice'),

    path('generate-json-data/', generate_json_data, name='generate_json_data'),
    path('json_data/', json_data, name='json_data'),
    path('process-data/', process_data, name='process_data'),
]
