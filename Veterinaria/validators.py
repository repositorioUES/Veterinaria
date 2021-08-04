from django.db import models
from .models import *

from datetime import datetime
from datetime import timedelta

from django.core.exceptions import ValidationError

def solo_Letras(value):
	
	letras = " 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú"

	for i in value:
		if i not in letras:
			raise ValidationError('Este dato no es válido, deben ser sólo letras')


def solo_Numeros(num):
	if isinstance(num, int): #Comprobamos si es int para pasarlo a str
		num = str(num)
	numeros = "0123456789-"

	for i in num:
		if i not in numeros:
			raise ValidationError('Solo se permiten números')

def validar_Fecha(f):

	hoy = datetime.now().date() #Definimos la fecha dehoy

	if f > hoy: # Si es una fecha MAYOR que HOY --> mala
		raise ValidationError('La fecha NO debe ser mayor que la de hoy')
	
	bottom = hoy - timedelta(days=36500)
	if f < bottom: # Si es una fecha MENOR que HACE 100 AÑOS (36500 DIAS)--> mala
		raise ValidationError('La fecha NO debe ser muy antigua')

def fecha_mayor(f):

	hoy = datetime.now().date() #Definimos la fecha dehoy

	if f < hoy: # Si es una fecha MENOR que HOY --> mala
		raise ValidationError('La fecha NO debe ser menor que la de hoy')

def formato_Dui(dui):
	dui = str(dui)
	numeros = "0123456789"

	if len(dui) == 10:
		for i in range(10):
			if i != 8:
				if dui[i] not in numeros:
					raise ValidationError('DUI no cumple el formato, debe ser ########-#')
			else:
				if dui[i] != "-":
					raise ValidationError('DUI no cumple el formato, debe ser ########-#')
	else:
		raise ValidationError('DUI no cumple el formato, debe ser ########-#')

def formato_Telefono(tel):
	tel = str(tel)
	numeros = "0123456789"

	if len(tel) == 9:
		for i in range(9):
			if i != 4:
				if tel[i] not in numeros:
					raise ValidationError('Teléfono NO cumple el formato, debe ser ####-####')
			else:
				if tel[i] != "-":
					raise ValidationError('Teléfono NO cumple el formato, debe ser ####-####')
	else:
		raise ValidationError('Teléfono NO cumple el formato, debe ser ####-####')

def formato_Hora(hora):
	hora = str(hora)
	charValidos = "0123456789: aApPmM"

	if len(hora) == 9:
		for i in range(9):
			if i != 4:
				if hora[i] not in charValidos:
					raise ValidationError('Teléfono NO cumple el formato, debe ser ####-####')
			else:
				if hora[i] != "-":
					raise ValidationError('Teléfono NO cumple el formato, debe ser ####-####')
	else:
		raise ValidationError('Teléfono NO cumple el formato, debe ser ####-####')