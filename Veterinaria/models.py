from django.db import models
from datetime import *
from django.utils import timezone
#from .validators import solo_Letras, solo_Numeros, fecha_Mayor_Que_Hoy, solo_ac_in
from django.core.exceptions import ValidationError

# Create your models here.

# Modelo del PACIENTE -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='images')
    nombre = models.CharField(max_length=50,help_text="Nombre del paciente")

    SEXO = (('m','Macho'),('h', 'Hembra'))# Estructura para la selección del sexo del paciente
    sexo = models.CharField(max_length=10, choices=SEXO, blank=True, help_text='Sexo del paciente')

    especie = models.CharField(max_length=50, help_text="Especie del paciente")
    raza = models.CharField(max_length=50,help_text="Raza del paciente")
    color = models.CharField(max_length=50,help_text="Color del paciente")
    fechaNacim = models.DateField(null=False, blank=True)
    observaciones = models.CharField(max_length=500,help_text="Las que considere peertinentes")

    # Booleano para determinar su el paciente esta activo o no
    activo = models.IntegerField(max_length=1, blank=True,  default=1)
    
    propietario = models.ForeignKey('Propietario', on_delete = models.SET_NULL, null=True)
    
    def __str__(self): #Para que retorne el nombre y no el Id
        return self.nombre
#FIN PACIENTE

# Modelo del PROPIETARIO -------------------------------------------------------------------
#Programador y Analista: Ruddy Alfredo Pérez

class Propietario(models.Model):
    dui = models.CharField(max_length=10, help_text="Número de DUI", primary_key=True)
    nombre = models.CharField(max_length=100,)
    apellido = models.CharField(max_length=100)
    fechaNacim = models.DateField(null=False, blank=True)
    edad = models.IntegerField(help_text="Se calculará automaticamente")
    direccion = models.CharField(max_length=100,help_text="Calle, Colonia, Cantón ...")
    departamento = models.ForeignKey('Departamento', on_delete = models.SET_NULL, null=True)
    municipio = models.ForeignKey('Municipio', on_delete = models.SET_NULL, null=True)
    correo = models.CharField(max_length=50,help_text="Correo Electrónico")
    telefono = models.CharField(max_length=50,help_text="Telefono de contacto")

    def __str__(self): #Para que retorne el nombre y no el Id
        return self.nombre
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