from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField 
# from datetime import datetime, date, timedelta
# from django.utils.timezone import now

# Create your models here.

class Rol(models.Model):
    # ID proporcionado por django
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Usuario(AbstractUser):
    # ID proporcionado por django
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    # Contraseña proporcionada por django
    rol = models.ForeignKey(Rol, on_delete=models.RESTRICT)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
    
class TicketState(models.Model):
    # ID proporcionado por django
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class TicketEntrada(models.Model):
    # ID proporcionado por django
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    entrace_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    patente = models.CharField(max_length=6, unique=True)
    state = models.ForeignKey(TicketState, on_delete=models.RESTRICT, default=1)
    price = models.FloatField(null=True, blank=True, default="20.0")
    
    def __str__(self) -> str:
        return f'{self.patente} {self.state} {self.date}'

class Protocolo(models.Model):
    # ID proporcionado por django
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    rut = models.CharField(max_length=10, unique=True)
    number = PhoneNumberField(region="CL", blank=False, null=True)
    patente = models.CharField(max_length=6)
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    date = models.DateField()
    description = models.TextField(max_length=45)

    def __str__(self) -> str:
        return f'{self.patente} {self.description}'
    

class TicketSalida(models.Model):
    # ID proporcionado por django
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    entrace_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    patente = models.CharField(max_length=6, unique=True)
    state = models.ForeignKey(TicketState, on_delete=models.RESTRICT, default=3)
    price = models.FloatField(null=True, blank=True, default="20.0")
    min_lapsed = models.PositiveIntegerField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.patente} {self.state}'