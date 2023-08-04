from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactoForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.


class ContactoUsuario(CreateView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('app.contacto:contacto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

    def form_valid(self, form):
        messages.success(self.request, 'CONSULTA ENVIADA CORRECTAMENTE.')
        return super().form_valid(form)
    
def contacto(request):
    data = {'form' : ContactoForm()}


    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Mensaje Enviado'
        else:
            data['form'] = formulario
    return render(request, 'contacto.html', data)
