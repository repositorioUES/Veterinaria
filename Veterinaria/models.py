from django.db import models
from datetime import *
from django.utils import timezone
from .validators import solo_Letras, solo_Numeros, validar_Fecha, fecha_mayor, formato_Dui, formato_Telefono
from django.core.exceptions import ValidationError

# Create your models here.

# Modelo del PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='fotos', null = True)
    nombrePac = models.CharField(max_length=50,help_text="", validators=[solo_Letras])

    SEXO = (('m','Macho'),('h', 'Hembra'))# Estructura para la selección del sexo del paciente
    sexo = models.CharField(max_length=10, choices=SEXO, blank=True, help_text='')

    especie = models.CharField(max_length=50, help_text="", validators=[solo_Letras])
    raza = models.CharField(max_length=50,help_text="", validators=[solo_Letras])
    color = models.CharField(max_length=50,help_text="", validators=[solo_Letras])
    fechaNacimPac = models.DateField(null=False, blank=True, validators=[validar_Fecha])
    observaciones = models.CharField(max_length=500, null = True, blank=True)
    fechaInscrip = models.DateField(auto_now_add = True)# fecha de inscripcion del paciente
    personaInscrip = models.CharField(max_length=70,help_text="", validators=[solo_Letras])

    # Booleano para determinar su el paciente esta activo o no
    activo = models.BooleanField(blank=True,  default=1)
    
    propietario = models.ForeignKey('Propietario', on_delete = models.SET_NULL, null=True)
    
    def __str__(self): #Para que retorne el nombre y no el Id
        return self.nombrePac + " (" + self.propietario.nombre + ")"
#FIN PACIENTE

# Modelo del PROPIETARIO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez

class Propietario(models.Model):
    dui = models.CharField(max_length=10, help_text="########-#", primary_key=True,validators=[formato_Dui])
    nombre = models.CharField(max_length=100, validators=[solo_Letras])
    apellido = models.CharField(max_length=100, validators=[solo_Letras])
    fechaNacim = models.DateField(validators=[validar_Fecha])
    edad = models.IntegerField(help_text="Se calculará automaticamente",validators=[solo_Numeros])
    direccion = models.CharField(max_length=100,help_text="Calle, Colonia, Cantón ...")
    departamento = models.ForeignKey('Departamento', on_delete = models.SET_NULL, null=True)
    municipio = models.ForeignKey('Municipio', on_delete = models.SET_NULL, null=True)
    correo = models.CharField(max_length=50,help_text="")
    telefono = models.CharField(max_length=9,help_text="####-####",validators=[formato_Telefono])

    def __str__(self): #Para que retorne el nombre y no el Id
        return self.nombre + " " + self.apellido
#FIN PROPIETARIO

# Modelo de DPARTAMENTO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Departamento(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100, help_text = "Ingrese un departamento")
    def __str__(self):
        return self.nombre
#FIN DEPARTAMENTO

# Modelo del MUNICIPIO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Municipio(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100, help_text = "Ingrese un municipio")
    departamento = models.ForeignKey('Departamento', on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre	
#FIN MUNICIPIO

# Modelo de CLINICA -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
class Clinica(models.Model):
    dueño = models.CharField(max_length=50, validators=[solo_Letras])
    nombre = models.CharField(max_length=60, validators=[solo_Letras])
    direccion = models.TextField()
    horarios = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9, validators=[formato_Telefono])
    servicios = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
#FIN CLINICA

class Empleado(models.Model):
    duiEmp = models.CharField(max_length=10, verbose_name="DUI", help_text="########-#",primary_key=True, validators=[formato_Dui])
    nombreEmp = models.CharField(max_length=100, validators=[solo_Letras])
    apellidoEmp = models.CharField(max_length=100, validators=[solo_Letras])
    telefonoEmp = models.CharField(max_length=10, help_text="####-####", validators=[formato_Telefono])
    cargo = models.CharField(max_length=50)
    salario = models.CharField(max_length=9, validators=[solo_Numeros])
    clinica = models.ForeignKey('Clinica', on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreEmp + " " + self.apellidoEmp

class Solicitudes(models.Model):
    solicitante = models.CharField(max_length=100, validators=[solo_Letras])
    nombreClinica = models.CharField(max_length=100, validators=[solo_Letras])
    direccionClinica = models.CharField(max_length=500)
    horariosClinica = models.CharField(max_length=500)
    telefonoClinica = models.CharField(max_length=10, help_text="####-####", validators=[formato_Telefono])
    serviciosClinica = models.CharField(max_length=500)

    def __str__(self):
        return self.solicitante + ": " + self.nombreClinica













































































# Modelo del HORARIO DE CONSULTA -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Horario(models.Model):
    id = models.AutoField(primary_key = True)
    hora = models.CharField(max_length=5)
    clinica = models.ForeignKey('Clinica', on_delete = models.PROTECT)
    activo = models.BooleanField(blank=True,  default=1)
    INDICADOR = (('am','AM'),('pm', 'PM'))# Estructura para la selección del indicador de la hora
    indicador = models.CharField(max_length=2, choices=INDICADOR, blank=True, help_text='')

    def __str__(self):
        return self.hora + " " + self.indicador
#FIN ORARIO DE CONSULTA

# Modelo de CITA -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Cita (models.Model):
    id = models.AutoField(primary_key = True)
    pacienteId = models.ForeignKey('Paciente', on_delete = models.PROTECT, null=True)
    clinica = models.ForeignKey('Clinica', on_delete = models.PROTECT)
    fechaCita = models.DateField(null=True, verbose_name="Fecha de Cita", validators=[fecha_mayor])# Fecha de la consulta
    horaCita = models.ForeignKey('Horario', null=True, on_delete=models.PROTECT, verbose_name="Hora de Cita")
    fechaCreacion = models.DateField(auto_now_add = True)# fecha de creación de la cita

    class Meta:
        unique_together =['fechaCita', 'horaCita']

    def unique_error_message(self, Cita, unique_check):
        if len(unique_check) != 1:
            return 'Esta HORA en esta FECHA ya esta ocupada, seleccione otra hora y/o fecha'
#FIN CITA

# Modelo de CONSULTA -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Consulta (models.Model):
    id = models.AutoField(primary_key = True)
    medico = models.CharField(max_length=70,null=False, validators=[solo_Letras])
    pacienteId = models.ForeignKey('Paciente', on_delete = models.PROTECT, null=True)
    edad = models.CharField(max_length=2, null=False, validators=[solo_Numeros])
    peso = models.CharField(max_length=10, null=False)
    fechaConsulta = models.DateField(auto_now_add = True)# fecha de creación de la consulta
    hora = models.CharField(max_length=10, null=False)
    observaciones = models.CharField(max_length=100, null = True, blank=True)
    medicamento = models.CharField(max_length=200, null = True, blank=True)
    examenes = models.CharField(max_length=200, null = True, blank=True)
    proximoCont = models.DateField(null=True, validators=[fecha_mayor])

#FIN CONSULTA

# Modelo de EXPEDIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez
class Expediente (models.Model):
    id = models.AutoField(primary_key = True)
    pacienteId = models.ForeignKey('Paciente', on_delete = models.PROTECT, null=True)
    clinica = models.ForeignKey('Clinica', on_delete = models.PROTECT, null=True)
    
    def __str__(self):
        i = str(id)
        return i
#FIN CONSULTA