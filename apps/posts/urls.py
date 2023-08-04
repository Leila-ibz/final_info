from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import ArticuloView, leer_articulo, crear_articulo, dropdown_menu_view

app_name= 'app.posts'

urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name='articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name='leer_articulo'),
    
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)