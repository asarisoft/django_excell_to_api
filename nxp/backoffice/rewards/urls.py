from django.urls import path, include
from .views import *

app_name = "rewards"
urlpatterns = [
    path("transactions/", transactions, name="transactions"),
    path("", redeem, name="redeem"),
]
