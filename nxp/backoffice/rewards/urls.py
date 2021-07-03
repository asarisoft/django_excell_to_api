from django.urls import path, include
from .views import *

app_name = "rewards"
urlpatterns = [
    path("transactions/", transactions, name="transactions"),
    path("", redeem, name="redeem"),
    path('<int:id>/redeem-detail/', redeem_detail, name='redeem_detail'),
    path('<int:id>/set-as-paid/', set_as_paid, name='set_as_paid'),
]
