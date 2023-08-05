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



class ArticuloForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']
