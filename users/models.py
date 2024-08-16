from django.db import models

# Create your models here.
class Persona(models.Model):
    ESTADO_CHOICES = [
        ('activo',"Activado"),
        ('inactivo',"Inactivo")
        ]
    name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fecha = models.DateField(auto_now=True)
    estado = models.CharField(max_length=100,choices=ESTADO_CHOICES,default='activo')
    def __str__(self):
        return self.name