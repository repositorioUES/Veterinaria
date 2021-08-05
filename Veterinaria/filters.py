from django.db.models import fields
import django_filters
from django_filters import CharFilter

from .models import *

class ClinicaFilter(django_filters.FilterSet):
    propietario = CharFilter(field_name='propietario', lookup_expr='icontains', label='Propietario')
    nombre = CharFilter(field_name='nombre', lookup_expr='icontains', label='Nombre de Clinica')

    class Meta:
        model = Clinica 
        fields = ['estado', 'propietario', 'nombre'] 


class ConsultorioFilter(django_filters.FilterSet):
    nombre = CharFilter(field_name='nombre', lookup_expr='icontains', label='Nombre de Consultorio')

    class Meta:
        model = Consultorio
        fields = ['estado', 'nombre']

class EmpleadoFilter(django_filters.FilterSet):
    nombreEmp = CharFilter(field_name='nombreEmp', lookup_expr='icontains', label='Nombre')
    clinica = CharFilter(field_name='clinica', lookup_expr='icontains', label='Clinica')
    consultorio = CharFilter(field_name='consultorio', lookup_expr='icontains', label='Consultorio')

    class Meta:
        model = Empleado 
        fields = ['nombreEmp', 'clinica', 'consultorio']