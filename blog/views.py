from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# class Indexviews(TemplateView):
#    template_name = 'index.html'

def Indexviews(request):
    return render(request, 'index.html')
