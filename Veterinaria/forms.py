from django import forms
from Veterinaria.models import *


class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = {
			'foto','nombre','propietario','sexo', 'especie','raza','color','fechaNacim','observaciones',
		}
		labels = {
			'foto':'Foto',
			'nombre':'Paciente',
            'propietario':'Propietario',
		    'sexo':'Sexo',
		    'especie':'Especie',
		    'raza':'Raza',
		    'color':'Color',
		    'fechaNacim':'Fecha de Nacimiento',
            'observaciones':'Observaciones',
		}	

		
class PropietarioForm(forms.ModelForm):
	class Meta:
		model = Propietario
		fields = {
			'dui','nombre', 'apellido','fechaNacim','edad','direccion','departamento','municipio','telefono','correo',
		}
		labels = {
			'dui':'Número de DUI',
			'nombre':'Nombre',
		    'fechaNacim':'Fecha de Nacimiento',
            'edad':'Edad',
            'direccion':'Dirección',
            'departamento':'Departamento',
            'municipio':'Municipio',
            'telefono':'Telefono',
            'correo':'Correo Electrónico',
		}