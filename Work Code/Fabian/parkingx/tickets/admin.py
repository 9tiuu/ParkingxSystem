from django.contrib import admin
from .models import Rol, Usuario, Protocolo

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Protocolo)