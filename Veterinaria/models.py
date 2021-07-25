from django.db import models
from datetime import *
from django.utils import timezone
from .validators import solo_Letras, solo_Numeros, validar_Fecha
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

    # Booleano para determinar su el paciente esta activo o no
    activo = models.IntegerField(blank=True,  default=1)
    
    propietario = models.ForeignKey('Propietario', on_delete = models.SET_NULL, null=True)
    
    def __str__(self): #Para que retorne el nombre y no el Id
        return self.nombrePac
#FIN PACIENTE

# Modelo del PROPIETARIO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez

class Propietario(models.Model):
    dui = models.CharField(max_length=10, help_text="########-#", primary_key=True,validators=[solo_Numeros])
    nombre = models.CharField(max_length=100, validators=[solo_Letras])
    apellido = models.CharField(max_length=100, validators=[solo_Letras])
    fechaNacim = models.DateField(validators=[validar_Fecha])
    edad = models.IntegerField(help_text="Se calculará automaticamente",validators=[solo_Numeros])
    direccion = models.CharField(max_length=100,help_text="Calle, Colonia, Cantón ...")
    departamento = models.ForeignKey('Departamento', on_delete = models.SET_NULL, null=True)
    municipio = models.ForeignKey('Municipio', on_delete = models.SET_NULL, null=True)
    correo = models.CharField(max_length=50,help_text="")
    telefono = models.CharField(max_length=9,help_text="####-####",validators=[solo_Numeros])

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
    id = models.IntegerField(primary_key = True)
    propietario = models.CharField(max_length=50, validators=[solo_Letras])
    nombre = models.CharField(max_length=60)
    direccion = models.TextField()
    horarios = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    servicios = models.CharField(max_length=100)
    fechaIngreso = models.DateField(auto_now_add=True, null=True)
    correoElectronico = models.CharField(max_length=200, null=True)
    ESTADO = (('Activa','Activa'),('Inactiva', 'Inactiva'))
    estado = models.CharField(max_length=10, choices=ESTADO, default="Activa")

    def __str__(self):
        return self.nombre
#FIN CLINICA

# Modelo de CONSULTORIO -------------------------------------------------------------------
#Programador y Analista: Christian Garcia
class Consultorio(models.Model):
    clinica = models.ForeignKey('Clinica', on_delete = models.CASCADE)
    nombre = models.CharField(max_length=60)
    direccion = models.TextField()
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    horarios = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    servicios = models.CharField(max_length=100)
    fechaIngreso = models.DateField(auto_now_add=True, null=True)
    correoElectronico = models.CharField(max_length=200, null=True)
    ESTADO = (('Activa','Activa'),('Inactiva', 'Inactiva'))
    estado = models.CharField(max_length=10, choices=ESTADO, default="Activa")

    def __str__(self):
        return self.nombre
#FIN CLINICA

class Empleado(models.Model):
    duiEmp = models.CharField(max_length=10, help_text="########-#",primary_key=True, validators=[solo_Numeros])
    nombreEmp = models.CharField(max_length=100, validators=[solo_Letras])
    apellidoEmp = models.CharField(max_length=100, validators=[solo_Letras])
    telefonoEmp = models.CharField(max_length=10, help_text="####-####", validators=[solo_Numeros])
    cargo = models.CharField(max_length=50)
    salario = models.CharField(max_length=9, validators=[solo_Numeros])
    consultorio = models.ForeignKey('Consultorio', on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreEmp + " " + self.apellidoEmp

class Solicitudes(models.Model):
    solicitante = models.CharField(max_length=100, validators=[solo_Letras])
    nombreClinica = models.CharField(max_length=100, validators=[solo_Letras])
    direccionClinica = models.CharField(max_length=500)
    horariosClinica = models.CharField(max_length=500)
    telefonoClinica = models.CharField(max_length=10, help_text="####-####", validators=[solo_Numeros])
    serviciosClinica = models.CharField(max_length=500)

    def __str__(self):
        return self.solicitante + ": " + self.nombreClinica