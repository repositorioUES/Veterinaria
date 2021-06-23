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

app_name = 'Veterinaria'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Veterinaria.urls')),
    path('registrarPaciente/', RegistrarPaciente.as_view(), name='registrar_paciente'),
    path('modificarPaciente/<int:pk>', ModificarPaciente.as_view(), name='modificar_paciente'),
    path('detallePaciente/<int:pk>', DetallePaciente.as_view(), name='detalle_paciente'),
    path('listadoPacientes/', ListadoPacientes.as_view(), name='listado_pacientes'),
    path('detallePropietario/<str:pk>', DetallePropietario.as_view(), name='detalle_propietario'),
    path('buscarPaciente/', BuscarPaciente, name='buscar_paciente'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT,}),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)