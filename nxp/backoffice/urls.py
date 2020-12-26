from django.urls import path, include
from .views import login_view, log_out, index

app_name = "backoffice"
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('log_out/', log_out, name='log_out'),
    path('formulir/', include('nxp.backoffice.formulir.urls', namespace='formulir')),
]
