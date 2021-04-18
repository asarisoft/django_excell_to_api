from django.urls import path, include
from .views import *

app_name = "serial_number"
urlpatterns = [
    path("", index, name="index"),
    path("generate", generate, name="generate"),
    # path("add/", add, name="add"),
    # path("<int:id>/edit", edit, name="edit"),
    # path("<int:id>/delete", delete, name="delete")
]
