"""ProyectoVeterinaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from Veterinaria.views import *
from Veterinaria.ajax import load_Municipios, load_Propietario, load_Paciente
from django.contrib.auth.decorators import login_required

app_name = 'Veterinaria'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Veterinaria.urls')),
    path('registrarPaciente/', login_required(RegistrarPaciente.as_view()), name='registrar_paciente'),
    path('modificarPaciente/<int:pk>', login_required(ModificarPaciente.as_view()), name='modificar_paciente'),
    path('detallePaciente/<int:pk>', login_required(DetallePaciente.as_view()), name='detalle_paciente'),
    path('listadoPacientes/', login_required(ListadoPacientes.as_view()), name='listado_pacientes'),
    path('detallePropietario/<str:pk>', login_required(DetallePropietario.as_view()), name='detalle_propietario'),
    path('buscarPaciente/', login_required(BuscarPaciente), name='buscar_paciente'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT,}),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ajax/load_Municipio/', load_Municipios, name='load_Municipio'),
    path('registrarEmpleado/', login_required(CrearEmpleado.as_view()), name='crear_empleado'),
    path('listadoEmpleados/', login_required(ListarEmpleados.as_view()), name='listado_empleados'),
    path('detalleEmpleado/<str:pk>', login_required(DetalleEmpleado.as_view()), name='detalle_empleado'),
    path('solicitudIngreso/', CrearSolicitud.as_view(), name='crear_solicitud'),
    path('solicitudEnviada/', SolicitudEnviada, name='solicitud_enviada'),
    path('listadoSolicitudes/', login_required(ListarSolicitudes.as_view()), name='listado_solicitudes'),
    path('detalleSolicitud/<int:pk>', login_required(DetalleSolicitud.as_view()), name='detalle_solicitud'),
    path('listadoCitas/', login_required(ListadoCitas.as_view()), name='listado_citas'),
    path('crearCita/', login_required(CrearCita.as_view()), name='crear_cita'),
    path('detalleCita/<int:pk>', login_required(DetalleCita.as_view()), name='detalle_cita'),
    path('modificarCita/<int:pk>', login_required(ModificarCita.as_view()), name='modificar_cita'),
    path('cancelarCita/<int:pk>/', login_required(CancelarCita.as_view()), name = 'cancelar_cita'),
    path('listadoHorarios/', login_required(ListadoHorarios.as_view()), name='listado_horarios'),
    path('crearHorario/', login_required(CrearHorario.as_view()), name='crear_horario'),
    path('modificarHorario/<int:pk>', login_required(ModificarHorario.as_view()), name='modificar_horario'),
    path('tipoRegistro/', login_required(TipoRegistro), name = 'tipo_registro'),
    path('registrarSoloPaciente/', login_required(RegistrarSoloPaciente.as_view()), name='registrar_solo_paciente'),
    path('registrarConsulta/', login_required(RegistrarConsulta.as_view()), name='registrar_consulta'),
    path('detalleConsulta/<int:pk>', login_required(DetalleConsulta.as_view()), name='detalle_consulta'),
    path('expediente/<int:pk>', login_required(DetalleExpediente), name='expediente'),
    path('ajax/load_Propietario/', load_Propietario, name='load_Propietario'),
    path('ajax/load_Paciente/', load_Paciente, name='load_Paciente'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)