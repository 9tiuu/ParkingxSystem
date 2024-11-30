from django.contrib import admin
from .models import Rol, Usuario, Protocolo, TicketEntrada, TicketState, TicketSalida

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Protocolo)
admin.site.register(TicketEntrada)
admin.site.register(TicketState)
admin.site.register(TicketSalida)