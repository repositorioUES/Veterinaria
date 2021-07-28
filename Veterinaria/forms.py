from django import forms
from .models import *
from Veterinaria.models import Paciente, Propietario, Empleado, Solicitudes
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
			 'activo','foto','nombrePac','sexo', 'especie','raza','color','fechaNacimPac','observaciones','personaInscrip',
		]
		labels = {
			'activo': 'Activo',
			'foto':'Foto *',
			'nombrePac':'Nombre de Paciente *',
		    'sexo':'Sexo *',
		    'especie':'Especie *',
		    'raza':'Raza *',
		    'color':'Color *',
		    'fechaNacimPac':'Fecha de Nacimiento *',
            'observaciones':'Observaciones',
			'personaInscrip':'Persona que Inscribió *'
		}
		widgets = {
			'observaciones':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
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
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = [
			'duiEmp','nombreEmp', 'apellidoEmp','telefonoEmp','cargo','salario','clinica',
		]
		labels = {
			'duiEmp':'Número de DUI *',
			'nombreEmp':'Nombre *',
			'apellidoEmp':'Apellido *',
            'telefonoEmp':'Telefono *',
            'cargo':'Puesto de Trabajo *',
			'salario':'Salario *',
			'clinica':'Clinica en que Trabaja *',
		}

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = Solicitudes
		fields = [
			'solicitante','nombreClinica', 'direccionClinica', 'horariosClinica', 'telefonoClinica','serviciosClinica',
		]
		labels = {
			'solicitabte':'Nonbre del Dueño*',
			'nombreClinica':'Nombre de la Clínica*',
			'direccionClinica':'Dirección*',
            'horariosClinica':'Horarios*',
            'telefonoClinica':'Telefono*',
			'serviciosClinica':'Servicios que Presta*',
		}
		widgets = {
			'horariosClinica':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
			'serviciosClinica':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
		}























































































class HorarioForm(forms.ModelForm):
	class Meta:
		model = Horario
		fields = [
			 'clinica','hora','indicador','activo',
		]
		labels = {
			'clinica':'Clínca *',
			'hora':'Hora *',
			'indicador':'Indicador *',
			'activo':'Activo ',
		}

class CitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = [
			 'pacienteId','clinica','fechaCita','horaCita',
		]
		labels = {
			'pacienteId':'Paciente *',
			'clinica':'Clínica *',
			'fechaCita':'Fecha de Cita *',
		    'horaCita':'Hora de Cita *',
		}
		widgets = {
			'fechaCita': DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control',}),
		}

class SoloPacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = [
			 'activo','foto','nombrePac','sexo', 'especie','raza','color','fechaNacimPac','observaciones','propietario','personaInscrip',
		]
		labels = {
			'activo': 'Activo',
			'foto':'Foto *',
			'nombrePac':'Paciente *',
		    'sexo':'Sexo *',
		    'especie':'Especie *',
		    'raza':'Raza *',
		    'color':'Color *',
		    'fechaNacimPac':'Fecha de Nacimiento *',
            'observaciones':'Observaciones',
			'propietario':'Propietario *',
			'personaInscrip':'Persona que Inscribió *'
		}
		widgets = {
			'observaciones':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
			'fechaNacimPac': DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control',}),
		}

class ConsultaForm(forms.ModelForm):
	class Meta:
		model = Consulta
		fields = [
			 'medico','pacienteId','edad','peso','hora','observaciones','medicamento','examenes','proximoCont',
		]
		labels = {
			'medico': 'Medico Veterinario *',
			'pacienteId':'Paciente *',
			'edad':'Edad *',
			'peso':'Peso *',
			'hora':'Hora *',
			'observaciones':'Observaciones',
			'medicamento':'Medicamentos',
			'examenes':'Exámenes',
			'proximoCont':'Proximo Control *',
		}
		widgets = {
			'observaciones':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
			'medicamento':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
			'examenes':forms.Textarea(attrs={'class':'form-contol','rows':'4'}),
			'proximoCont': DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control',}),
		}

class ExpedienteForm(forms.ModelForm):
	class Meta:
		model = Expediente
		fields = [
			 'clinica',
		]
		labels = {
			'clinica':'Clínica *',
		}