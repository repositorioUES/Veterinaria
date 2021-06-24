from django.http import JsonResponse

from django.db.models import Q
from django.shortcuts import render
from .models import *


def load_Municipios(request):
	depId = request.GET.get('depId')
	municipios = Municipio.objects.filter(departamento_id = depId)
	
	return render(request, 'hr/mun_dropdown_list.html', context={'mun': municipios})

