from django.urls import path
from . import views
from .views import ContactoUsuario


app_name = 'app.contacto'


urlpatterns = [
     path('', ContactoUsuario.as_view(), name='contacto'),
     
]
