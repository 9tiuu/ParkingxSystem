from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Rol(models.Model):
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
    # Contraseña proporcionada por Django
    rol = models.ForeignKey(Rol, on_delete=models.RESTRICT)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

# Ticket de entrada

# Ticket de salida

# Protocolos de seguridad