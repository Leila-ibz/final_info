from django.contrib import admin
from .models import Categoria, Articulo, Comentario
# Register your models here.


@admin.register(Articulo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumen', 'contenido', 'fecha_publicacion', 'imagen', 'autor' , 'estado', 'categoria', 'publicado')


admin.site.register(Comentario)

admin.site.register(Categoria)  