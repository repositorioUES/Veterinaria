from django import forms
from django.views.generic.edit import View, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from Veterinaria.models import *
from Veterinaria.forms import *
from datetime import *
from django.views.generic import TemplateView
from django.db.models import Q
from django.shortcuts import render, redirect, render,get_object_or_404
from .forms import CustomUserCreationForm, ClinicaForm
from .filters import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Vista REGISTRAR USUARIO -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
def registro(request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Registro exitoso")
            return redirect(to="index")
        data["form"]=formulario
    return render(request, 'registration/registro.html', data)

# Vista REGISTRAR CLINICA -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def registrar_clinica(request):

    data = {
        'form' : ClinicaForm()
    }

    if request.method == 'POST':
        formulario=ClinicaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Clinica registrada exitosamente")
            return redirect(to="listar_clinica")
        else:
            data['form'] = formulario
    return render(request, 'clinica/agregarClinica.html',data)

# Vista LISTAR CLINICA  -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def listar_clinica(request):
    clinicas = Clinica.objects.all()
    page = request.GET.get('page',1)

    filter = ClinicaFilter(request.GET, queryset=clinicas)
    clinicas = filter.qs

    try:
        paginator = Paginator(clinicas,10)
        clinicas = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': clinicas,
        'paginator': paginator,
        'filter' : filter
    }

    return render(request, 'clinica/listarClinica.html', data)

# Vista MODIFICAR CLINICA  -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def modificar_clinica(request, id):

    clinica = get_object_or_404(Clinica, id=id)
    data ={
        'form' : ClinicaForm(instance=clinica)
    }

    if request.method == 'POST':
        formulario = ClinicaForm(data=request.POST, instance=clinica)
        if formulario.is_valid():
            formulario.save()
            messages.success(request," Modificado correctamente")
            return redirect(to="listar_clinica")
        data['form'] = formulario
    return render(request, 'clinica/modificarClinica.html', data)

# Vista ELIMINAR CLINICA  -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def eliminar_clinica(request, id):
    clinica = get_object_or_404(Clinica, id=id)
    clinica.delete()
    messages.success(request," Clinica eliminada correctamente")
    return redirect(to="listar_clinica")

# Vista REGISTRAR CONSULTORIO -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def registrar_consultorio(request, id):
    clinica = Clinica.objects.get(id=id)
    data = {
        'form' : ConsultorioForm(initial={'clinica': clinica})
    }

    if request.method == 'POST':
        formulario=ConsultorioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Consultorio registrado exitosamente")
            return redirect('listar_consultorio', clinica.id )
        else:
            data['form'] = formulario
    return render(request, 'consultorio/agregarConsultorio.html',data)

# Vista LISTAR CONSULTORIO  -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def listar_consultorio(request,id):
    clinica = Clinica.objects.get(id=id)
    consultorios = clinica.consultorio_set.all()

    filter = ConsultorioFilter(request.GET, queryset=consultorios)
    consultorios = filter.qs

    data = {
        'clinica' : clinica,
        'consultorios' : consultorios,
        'filter' : filter
    }
    
    return render(request, 'consultorio/listarConsultorio.html', data)

# Vista MODIFICAR CONSULTORIO  -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def modificar_consultorio(request, id):

    consultorio = get_object_or_404(Consultorio, id=id)
    data ={
        'form' : ConsultorioForm(instance=consultorio)
    }

    if request.method == 'POST':
        formulario = ConsultorioForm(data=request.POST, instance=consultorio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request," Consultorio modificado correctamente")
            return redirect('listar_consultorio', consultorio.clinica.id)
        data['form'] = formulario
    return render(request, 'consultorio/modificarConsultorio.html', data)

# Vista ELIMINAR CONSULTORIO  -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
@login_required
def eliminar_consultorio(request, id):
    consultorio = get_object_or_404(Consultorio, id=id)
    consultorio.delete()
    messages.success(request," Consultorio eliminado correctamente")
    return redirect('listar_consultorio', consultorio.clinica.id)

# Vista REGISTRAR PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class RegistrarPaciente(CreateView):
    model = Paciente
    template_name = 'Plantillas/registrarPaciente.html'
    form_class = PacienteForm
    second_form_class = PropietarioForm
    success_url = reverse_lazy('listado_pacientes')

    def get_context_data (self , **kwargs):
        context = super(RegistrarPaciente, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post (self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            paciente = form.save(commit=False)
            paciente.propietario = form2.save()
            paciente.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

# Vista MODIFICAR PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class ModificarPaciente(UpdateView):
    model = Paciente
    second_model = Propietario
    template_name = 'Plantillas/modificarPaciente.html'
    form_class = PacienteForm
    second_form_class = PropietarioForm
    success_url = reverse_lazy('listado_pacientes')

    def get_context_data (self , **kwargs):
        context = super(ModificarPaciente, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        paciente = self.model.objects.get(id=pk)
        propietario = self.second_model.objects.get(dui=paciente.propietario_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=propietario)
        context['id'] = pk
        return context
    
    def post (self, request, *args, **kwargs):
        self.object = self.get_object
        id_paciente = kwargs['pk']
        paciente = self.model.objects.get(id=id_paciente)
        propietario = self.second_model.objects.get(dui=paciente.propietario_id)
        form = self.form_class(request.POST, request.FILES, instance=paciente)
        form2 = self.second_form_class(request.POST, request.FILES or None, instance=propietario)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            #paciente.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))
    
# Vista DETALLE DE PACIENTES -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class DetallePaciente(DetailView):
    model = Paciente
    template_name = 'Plantillas/detallePaciente.html'
    form_class = PacienteForm
    context_object_name = 'paciente'

# Vista LSITADO DE PACIENTES -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class ListadoPacientes(ListView):
    model = Paciente
    template_name = 'Plantillas/listadoPacientes.html'
    context_object_name = 'pacientes'

# Vista BUSCAR PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
def BuscarPaciente(request):
    queryset = request.GET.get('buscar')
    context={}
    if queryset:
        pacientes = Paciente.objects.filter(nombrePac__icontains=queryset)
        if pacientes:
            context = {'pacientes':pacientes}
            print(pacientes)
        else:
            p = Propietario.objects.filter(Q(nombre__icontains=queryset) | Q(apellido__icontains=queryset) | Q(dui=queryset)).first()
            if p:
                pacientes = Paciente.objects.filter(propietario_id=p.dui)
                context = {'pacientes':pacientes}
                print(p)
                print(pacientes)
        
    return render(request,'Plantillas/buscarPaciente.html', context)

# Vista DETALLE DE PROPIETARIO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class DetallePropietario(DetailView):
    model = Propietario
    template_name = 'Plantillas/detallePropietario.html'
    form_class = PropietarioForm
    context_object_name = 'prop'





class CrearEmpleado(CreateView):
    model = Empleado
    template_name = 'Plantillas/crearEmpleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('listado_empleados')

class ListarEmpleados(ListView):
    model = Empleado
    template_name = 'Plantillas/listadoEmpleados.html'
    context_object_name = 'empleados'

class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = 'Plantillas/detalleEmpleado.html'
    form_class = EmpleadoForm
    context_object_name = 'empleado'



class CrearSolicitud(CreateView):
    model = Solicitudes
    template_name = 'Plantillas/crearSolicitud.html'
    form_class = SolicitudForm
    success_url = reverse_lazy('solicitud_enviada')

def SolicitudEnviada(request):
    return render(request, 'Plantillas/solicitudEnviada.html')

class ListarSolicitudes(ListView):
    model = Solicitudes
    template_name = 'Plantillas/listadoSolicitudes.html'
    context_object_name = 'solicitudes'

class DetalleSolicitud(DetailView):
    model = Solicitudes
    template_name = 'Plantillas/detalleSolicitud.html'
    form_class = SolicitudForm
    context_object_name = 'solicitud'