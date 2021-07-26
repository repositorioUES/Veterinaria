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