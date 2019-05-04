from django.shortcuts import render
from django.views.generic import ListView
from .models import RegistroEnergia

# Create your views here.
class IndexView(ListView):
    context_object_name = 'registros_energia'
    queryset = RegistroEnergia.objects.all()
    template_name = 'registro/index.html'
