from django import forms
from .models import *
from Veterinaria.models import Paciente, Propietario
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Clinica

class DateInput(forms.DateInput):
	input_type = 'date'


class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = [
			'foto','nombrePac','sexo', 'especie','raza','color','fechaNacimPac','observaciones',
		]
		labels = {
			'foto':'Foto*',
			'nombrePac':'Paciente*',
		    'sexo':'Sexo*',
		    'especie':'Especie*',
		    'raza':'Raza*',
		    'color':'Color*',
		    'fechaNacimPac':'Fecha de Nacimiento*',
            'observaciones':'Observaciones',
		}
		widgets = {
			'observaciones':forms.Textarea(attrs={'class':'form-contol'}),
			'fechaNacimPac': DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control',}),
		}


		
class PropietarioForm(forms.ModelForm):
	class Meta:
		model = Propietario
		fields = [
			'dui','nombre', 'apellido','fechaNacim','edad','direccion','departamento','municipio','telefono','correo',
		]
		labels = {
			'dui':'Número de DUI*',
			'nombre':'Nombre*',
			'apellido':'Apellido*',
		    'fechaNacim':'Fecha de Nacimiento*',
            'edad':'Edad*',
            'direccion':'Dirección*',
            'departamento':'Departamento*',
            'municipio':'Municipio*',
            'telefono':'Telefono*',
            'correo':'Correo Electrónico*',
		}
		widgets = {
			'edad':forms.TextInput(attrs={'class':'form-contol', 'disabled':'True'}),
			'fechaNacim': DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control'}),
		}

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name", "email", "password1","password2"]
class ClinicaForm(forms.ModelForm):

    class Meta:
        model = Clinica
        fields = '__all__'
