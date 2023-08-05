from django.db import models
from django.utils import timezone
import random
import os
from functools import partial
from django.conf import settings


#Categoria:
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    
    
# Articulo
def get_random_avatar_filename(instance, filename):
    return f'articulo/avatars/{filename}'

def default_avatar():
    return 'articulo/avatar/avatar3_default.jpg'

class Articulo(models.Model):
    # Campos existentes
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='posts')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default = 'Sin categoria')
    publicado = models.DateTimeField(default=timezone.now)
    
    # Nuevos campos
    avatar = models.ImageField(null=True, blank=True, upload_to=get_random_avatar_filename, default=default_avatar)
    nickname = models.CharField(max_length=30, default="Sin Nickname")


    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parent=False):
        self.imagen.delete()

        if self.avatar: 
            self.avatar.delete()
        super().delete()


class Comentario(models.Model):
    posts = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto