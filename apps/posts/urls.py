from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import reverse_lazy



from . import views
from .views import *

app_name= 'app.posts'

urlpatterns = [
    path('articulos/', ArticuloView.as_view(), name='articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name='leer_articulo'),
    # path('leer_articulo/<int:id>', views.PostDetailView.as_view(), name='leer_articulo'),
    
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('articulos/categoria', CategoriaCreateView.as_view(), name= 'crear_categoria'),
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>/delete', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('posts/<int:pk>/modificar/',PostUpdateView.as_view(), name= 'post_update'),
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)