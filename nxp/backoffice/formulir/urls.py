from django.urls import path, include
from .views import *

app_name = "formulir"
urlpatterns = [
    path("", index, name="index"),
    # path("add/", add, name="add"),
    # path("<int:id>/edit", edit, name="edit"),
    # path("<int:id>/delete", delete, name="delete")
]
