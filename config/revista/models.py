from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"

class Personas(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, related_name='usuarios')
    personas  = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='personas')
    active = models.BooleanField(default=True)
    av_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
  
    def __str__(self):
        return f"{self.username}"
    
class Revisar(models.Model):
    rating= models.PositiveIntegerField(validators=[MinValueValidator(1), MinValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="revisars")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) +  " | " + self.usuario.username