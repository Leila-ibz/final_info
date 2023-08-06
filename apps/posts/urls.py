from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name= 'app.posts'

urlpatterns = [
    path('articulos/', views.ArticuloView.as_view(), name='articulos'),
    path('leer_articulo/<int:id>', views.leer_articulo, name='leer_articulo'),
    # path('leer_articulo/<int:id>', views.PostDetailView.as_view(), name='leer_articulo'),
    
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('articulos/categoria', views.CategoriaCreateView.as_view(), name= 'crear_categoria'),
    path('categoria/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>/delete', views.CategoriaDeleteView.as_view(), name='categoria_delete'),


    path('posts/<int:post_id>/editar_comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('posts/<int:post_id>/eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)