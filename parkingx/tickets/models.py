from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Rol(models.Model):
    # ID proporcionado por django
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Usuario(AbstractUser):
    # ID proporcionado por django
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, unique=True)
    # Contraseña proporcionada por django
    rol = models.ForeignKey(Rol, on_delete=models.RESTRICT)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class TicketE(models.Model): # POR TERMINAR
    # ID proporcionado por django
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    entrace_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    patente = models.CharField(max_length=6)
    # Relacionar estado de ticket (POR HACER)
    price = models.FloatField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.patente

# Ticket de salida

class Protocolo(models.Model):
    # ID proporcionado por django
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    rut = models.CharField(max_length=10)
    number = models.CharField(max_length=9)
    patente = models.CharField(max_length=6)
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    date = models.DateField()
    description = models.TextField(max_length=45)

    def __str__(self) -> str:
        return f'{self.patente} {self.description}'
