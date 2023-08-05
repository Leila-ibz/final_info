from django import forms
from .models import Articulo, Comentario, Categoria

class ArticuloForm(forms.ModelForm):
    class Meta: 
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

