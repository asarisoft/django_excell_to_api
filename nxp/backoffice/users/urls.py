from django.urls import path, include
from .views import *

app_name = "users"
urlpatterns = [
    path("", users, name="users"),
    path('<int:id>/user-detail/', user_detail, name='user_detail'),
]
