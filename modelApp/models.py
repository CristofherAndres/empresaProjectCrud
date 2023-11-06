from django.db import models

# Create your models here.

""" Crear clase de Estado """
class Estado(models.Model):
    nombre      = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre      = models.CharField(max_length=50)
    telefono    = models.CharField(max_length=12)
    email       = models.CharField(max_length=50)
    """ Agregar un estado """
    estado      = models.ForeignKey(Estado, on_delete=models.CASCADE)