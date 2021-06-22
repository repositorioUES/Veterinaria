from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from Veterinaria.models import *
from Veterinaria.forms import *
from datetime import *
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.db.models import Q

# Create your views here.
def index (request):
    return render(request, 'index.html')


# Vista REGISTRAR PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class RegistrarPaciente(CreateView):
    template_name = 'Plantillas/registrarPaciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('admon:listado_pacientes')

# Vista REGISTRAR PROPIETARIO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class RegistrarPropietario(CreateView):
    template_name = 'Plantillas/registrarPropietario.html'
    form_class = PropietarioForm
    success_url = reverse_lazy('admon:listado_pacientes')

# Vista LSITADO DE PACIENTES -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class ListadoPacientes(ListView):
    model = Paciente
    template_name = 'Plantillas/listadoPacientes.html'
    context_object_name = 'pacientes'