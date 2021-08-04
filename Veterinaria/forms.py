from django import forms
from django.contrib.admin import widgets
from django.forms import fields
from Veterinaria.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
			'edad':forms.TextInput(attrs={'class':'form-contol'}),
			'fechaNacim': DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control'}),
		}

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name", "email", "password1","password2"]

class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = [
			'propietario','nombre','direccion', 'horarios', 'telefono', 'correoElectronico', 'servicios', 'estado',
		]

class ConsultorioForm(forms.ModelForm):

    class Meta:
        model = Consultorio
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = [
			'duiEmp','nombreEmp', 'apellidoEmp','telefonoEmp','cargo','salario','consultorio',
		]
		labels = {
			'duiEmp':'Número de DUI*',
			'nombreEmp':'Nombre*',
			'apellidoEmp':'Apellido*',
            'telefonoEmp':'Telefono*',
            'cargo':'Cargo que Desempeña*',
			'salario':'Salario*',
			'consultorio':'Consultorio en que Trabaja*',
		}

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = Solicitudes
		fields = [
			'solicitante','nombreClinica', 'direccionClinica', 'horariosClinica', 'telefonoClinica','serviciosClinica',
		]
		labels = {
			'solicitante':'Nonbre del Dueño*',
			'nombreClinica':'Nombre de la Clínica*',
			'direccionClinica':'Dirección*',
            'horariosClinica':'Horarios*',
            'telefonoClinica':'Telefono*',
			'serviciosClinica':'Servicios que Presta*',
		}
		widgets = {
			'horariosClinica':forms.Textarea(attrs={'class':'form-contol'}),
			'serviciosClinica':forms.CheckboxSelectMultiple(),
		}

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = [
			'nombreServicio','descServicio','catServicio',
		]
		labels = {
			'nombreServicio':'Nombre del servicio',
			'descServicio':'Descripción',
			'catServicio':'Categoria',
		}
		widgets = {
			'descServicio':forms.Textarea(attrs={'class':'form-control', 'rows':'4'}),
		}