from django.contrib import admin
from django.urls import path, include
from .views import Indexviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

# ACA LE AVISA QUE TIENE QUE IR A BUSCAR LA URL DE LA APLICACION

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Indexviews, name='index'),
    path('posts/', include('apps.posts.urls')),
    path('contacto/', include('apps.contacto.urls')),
    path('usuario/', include('apps.usuario.urls')),
    # path('', include('django.contrib.auth.urls')),
    # path('posts/', include('apps.posts.urls', namespace='crear_articulo')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)