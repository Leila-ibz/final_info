from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import Group
# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'REGISTRO EXITOSO. POR FAVOR INICIA SESIÓN.')
        form.save()

        return redirect('app.usuario:registrar')
    

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    

    def get_success_url(self):
        messages.success(self.request, 'INICIO DE SESIÓN EXITOSO. ¡BIENVENID@!')
        return reverse('app.posts:articulos') 
    



    

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Cambia 'inicio' por la URL a la que quieres redirigir después del inicio de sesión exitoso
            else:
                context = {'form': form, 'error': 'Credenciales incorrectas'}
                return render(request, 'mytest/login.html', context)
    else:
        form = LoginForm()
    return render(request, 'mytest/login.html', {'form': form})



class LogoutUsuario(LogoutView):
    # template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, '¡SU CUENTA HA SIDO CERRADA CORRECTAMENTE! ¡HASTA LUEGO!')

        return reverse('app.usuario:login')
    

