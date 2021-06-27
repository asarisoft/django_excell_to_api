from django.urls import path, include
from .views import *

app_name = "rewards"
urlpatterns = [
    path("", redeem, name="redeem"),
]
