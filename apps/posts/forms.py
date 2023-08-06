from django import forms
from .models import Articulo, Comentario, Categoria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder,Field
# class ComentarioForm(forms.ModelForm):
#     class Meta:
#         model = Comentario
#         fields = ['texto']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            # Ajusta el ancho
            'texto': forms.Textarea(attrs={'rows': 6, 'style': 'width: 1200px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'container'
        self.helper.layout = Layout(
            Field('texto'),
            ButtonHolder(
                Submit('submit', 'Enviar comentario',
                       css_class='btn btn-primary'),
            )
        )

        self.fields['texto'].label = ''




# class ArticuloForm(forms.ModelForm):
#     # categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
 
#     class Meta:
#         model = Articulo
#         fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']
# class NuevaCategoriaForm(forms.ModelForm):
#     class Meta:
#         model = Categoria
#         fields = '__all__'


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
