from django.contrib import admin
from .models import Rol, Usuario, Protocolo, TicketE

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Protocolo)
admin.site.register(TicketE)