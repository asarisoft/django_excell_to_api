from django.urls import path
from .views import *

app_name = "frontend"
urlpatterns = [
    path('', index, name='index'),
    path('post-formulir/', post_formulir, name='post_formulir'),
]
