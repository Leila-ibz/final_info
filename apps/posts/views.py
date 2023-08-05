from django.shortcuts import render
from .models import Articulo, Comentario, Categoria
from django.views import View
from .forms import ArticuloForm
from .forms import ComentarioForm
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#asd

#!asd
# vista basada en clases
class ArticuloView(View):
    template_name= 'articulo.html'
#Obtener parámetro para filtrar por categoría mediante url
    def get(self, request):
        categoria_id = request.GET.get("categoria_id",None)
        if categoria_id is None:
            articulos = Articulo.objects.all()
        else:
            articulos = Articulo.objects.filter(categoria__id = categoria_id)
        opciones_dropdown = Categoria.objects.all()    
        return render(request, 'articulo.html', {'articulos' : articulos,'opciones_dropdown' : opciones_dropdown, 'categoria_filtrada': categoria_id},)


def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return i
    return None

def leer_articulo(request, id):
    articulo = Articulo.objects.filter(id = id).first()
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = id
            comentario.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form =  ComentarioForm() 
    context = {
        'articulos': articulo,
        "form" : form
    }

    return render (request, 'articulo_individual.html', context)

#Mostrar categorías
def mostrar_articulos(request):
    categorias = Categoria.objects.all()
    return render(request, 'articulo.html', {'categorias': categorias})

def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return i
    return None

def dropdown_menu_view(request):
    # Aquí puedes agregar la lógica para obtener las opciones del dropdown
    opciones_dropdown = ['Opción 1', 'Opción 2', 'Opción 3']

    return render(request, 'articulo.html', {'opciones_dropdown': opciones_dropdown})



#crear articulo !

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save()

            return HttpResponseRedirect(reverse("app.posts:leer_articulo", args=[articulo.id]))
    else:
        form = ArticuloForm()
        return render(request, 'publicar.html', {'form' : form})       

 



class PostDetailView(DetailView):
    model = Articulo
    template_name = "posts/articulo_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Articulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ComentarioForm() 

        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.post_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:articulo_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html'
    success_url = 'comentario/comentarios/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.post_id =self.kwargs ['posts_id']
        return super().form_valid(form)
