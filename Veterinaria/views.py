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
from .models import Clinica
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
            messages.success(request,"Registro exitoso")
            return redirect(to="index")
        data["form"]=formulario
    return render(request, 'registration/registro.html',data)

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
            messages.success(request,"Registro exitoso")
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

    try:
        paginator = Paginator(clinicas,5)
        clinicas = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': clinicas,
        'paginator': paginator
    }

    return render(request, 'clinica/listarClinica.html',data)

# Vista REGISTRAR PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class RegistrarPaciente(CreateView):
    model = Paciente
    template_name = 'Plantillas/registrarPaciente.html'
    form_class = PacienteForm
    second_form_class = PropietarioForm
    third_form_class = ExpedienteForm
    success_url = reverse_lazy('listado_pacientes')

    def get_context_data (self , **kwargs):
        context = super(RegistrarPaciente, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context
    
    def post (self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST, request.FILES or None)
        form3 = self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            paciente = form.save(commit=False)
            paciente.propietario = form2.save()
            paciente.activo = 1
            expediente = form3.save(commit=False)
            expediente.pacienteId = form.save()
            expediente.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2, form3 = form3))


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
        else:
            p = Propietario.objects.filter(Q(nombre__icontains=queryset) | Q(apellido__icontains=queryset) | Q(dui=queryset))
            if p:
                for prop in p:
                    pacientes |= Paciente.objects.filter(propietario_id=prop.dui)
                context = {'pacientes':pacientes}
        
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

































































def TipoRegistro(request):
    return render(request, 'Plantillas/tipoRegistro.html')

class RegistrarSoloPaciente(CreateView):
    model = Paciente
    template_name = 'Plantillas/registrarSoloPaciente.html'
    form_class = SoloPacienteForm
    second_form_class = ExpedienteForm
    success_url = reverse_lazy('listado_pacientes')

    def get_context_data (self , **kwargs):
        context = super(RegistrarSoloPaciente, self).get_context_data(**kwargs)
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
            expediente = form2.save(commit=False)
            form.activo = 1
            expediente.pacienteId = form.save()
            expediente.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

def PacientesInactivos(request):
    pacientes = Paciente.objects.filter(activo = 0)
    return render(request,'Plantillas/pacientesInactivos.html', {'pacientes':pacientes})

##  CITAS-------------------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class CrearCita(CreateView):
    model = Cita
    template_name = 'Plantillas/crearCita.html'
    form_class = CitaForm
    success_url = reverse_lazy('listado_citas')

class ModificarCita(UpdateView):
    model = Cita
    template_name = 'Plantillas/modificarCita.html'
    form_class = CitaForm
    success_url = reverse_lazy('listado_citas')

def ListadoCitas(request):
    hoy = datetime.now().date() # Fecha de hoy
    citasHoy = Cita.objects.filter(fechaCita__contains = hoy) # Citas SOLO de HOY
    citas = Cita.objects.filter(fechaCita__gt = hoy) # Citas a Futuro
    return render(request,'Plantillas/listadoCitas.html', {'citasHoy':citasHoy,'citas':citas})

# Vista BUSCAR CITA -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
def BuscarCita(request):
    pac = request.GET.get('buscar') # Filtro por paciente
    context={}
    hoy = datetime.now().date() # Fecha de hoy

    if pac: # Si mandamos info del paceiente
        paciente = Paciente.objects.filter(nombrePac__iexact=pac).first()
        if paciente:
            citasHoy = Cita.objects.filter(fechaCita__contains = hoy).filter(pacienteId=paciente.id) # Cita para Hoy
            citasFuturo = Cita.objects.filter(fechaCita__gt = hoy).filter(pacienteId=paciente.id) # Citas a Futuro
            citasPasado = Cita.objects.filter(fechaCita__lt = hoy).filter(pacienteId=paciente.id) # Citas ya Pasadas
            citaFecha = None
            context = {'citasHoy':citasHoy, 'citasFuturo':citasFuturo,'citasPasado':citasPasado,'citaFecha':citaFecha}
        else:
            citaFecha = Cita.objects.filter(fechaCita__icontains = pac)
            print(citaFecha)
            context = {'citaFecha':citaFecha}
        
    return render(request,'Plantillas/buscarCita.html', context)

class DetalleCita(DetailView):
    model = Cita
    template_name = 'Plantillas/detalleCita.html'
    form_class = CitaForm
    context_object_name = 'cita'

class DetalleCitaPasada(DetailView):
    model = Cita
    template_name = 'Plantillas/detalleCitaPasada.html'
    form_class = CitaForm
    context_object_name = 'cita'

class CancelarCita(DeleteView):
    template_name = 'Plantillas/cancelarCita.html'
    model = Cita
    success_url = reverse_lazy('listado_citas')

## HORARIOS-------------------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class CrearHorario(CreateView):
    model = Horario
    template_name = 'Plantillas/crearHorario.html'
    form_class = HorarioForm
    success_url = reverse_lazy('listado_horarios')

class ModificarHorario(UpdateView):
    model = Horario
    template_name = 'Plantillas/modificarHorario.html'
    form_class = HorarioForm
    success_url = reverse_lazy('listado_horarios')

class ListadoHorarios(ListView):
    model = Horario
    template_name = 'Plantillas/listadoHorarios.html'
    context_object_name = 'horarios'

def HorariosInactivos(request):
    horarios = Horario.objects.filter(activo = 0)
    return render(request,'Plantillas/horariosInactivos.html', {'horarios':horarios})

## CONSULTA-------------------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class RegistrarConsulta(CreateView):
    model = Consulta
    template_name = 'Plantillas/registrarConsulta.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('listado_pacientes')   
    
class DetalleConsulta(DetailView):
    model = Consulta
    template_name = 'Plantillas/detalleConsulta.html'
    form_class = ConsultaForm
    context_object_name = 'consulta'

## EXPEDIENTE-------------------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
def DetalleExpediente (request, pk):
    if request.method == 'GET':
        exp = Expediente.objects.filter(pacienteId_id = pk).first()
        consultas = Consulta.objects.filter(pacienteId_id = pk)

    return render(request, 'Plantillas/detalleExpediente.html', {'exp':exp,'cons':consultas})