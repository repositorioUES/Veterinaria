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
from Veterinaria.ajax import load_Municipios
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

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)