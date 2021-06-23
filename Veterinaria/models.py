from django.db import models

# Create your models here.

class Clinica(models.Model):
    dueño = models.CharField(max_length=50)
    nombre = models.CharField(max_length=60)
    direccion = models.TextField()
    horarios = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    servicios = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
