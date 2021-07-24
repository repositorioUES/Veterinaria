from django.http import JsonResponse

from django.db.models import Q
from django.shortcuts import render
from .models import *


def load_Municipios(request):
	depId = request.GET.get('depId')
	municipios = Municipio.objects.filter(departamento_id = depId)
	
	return render(request, 'hr/mun_dropdown_list.html', context={'mun': municipios})

def load_Propietario(request):
	propId = request.GET.get('propId')
	propietarios = Propietario.objects.filter(Q(nombre__icontains=propId) | Q(apellido__icontains=propId) | Q(dui=propId))

	return render(request, 'hr/prop_dropdown_list.html', context={'prop': propietarios})

def load_Paciente(request):
	filtro = request.GET.get('filtro')
	context = {}
	pac = Paciente.objects.filter(nombrePac__icontains = filtro)
	if pac:
		context ={'pac':pac}
	else:
		prop = Propietario.objects.filter(Q(nombre__icontains=filtro) | Q(apellido__icontains=filtro) | Q(dui=filtro))
		for p in prop:
			pac |= Paciente.objects.filter(propietario_id = p.dui)
		context ={'pac':pac}
	return render(request, 'hr/pac_dropdown_list.html', context)