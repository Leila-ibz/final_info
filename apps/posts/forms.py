from django import forms
from .models import Articulo, Comentario, Categoria
<<<<<<< HEAD

=======
>>>>>>> 668d66a5229526ca807cc44b0db86cc82f085b32

class ArticuloForm(forms.ModelForm):
    class Meta: 
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

<<<<<<< HEAD


class ArticuloForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']
=======
class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

>>>>>>> 668d66a5229526ca807cc44b0db86cc82f085b32
