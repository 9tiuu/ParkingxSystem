from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib import messages

from .models import Rol, Usuario, Protocolo, TicketE, TicketState
from .forms import RolForm, UsuarioForm, UserUpdateForm, ProtocoloForm, TicketEForm, TicketEUpdateForm, TicketStateForm, TicketEStateForm

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# ----------------------------------- # HOME

@login_required
def Home(request):
    return render(request, 'tickets/base.html')

# ----------------------------------- # ROLES

@method_decorator(login_required, name='dispatch')
class CreateRol(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'tickets/roluser_create.html'
    success_url = reverse_lazy('listrol')

    def form_valid(self, form):
        messages.success(self.request, '¡Rol Agregado con exito!')
        return super().form_valid(form)
    
    
class ListRol(ListView):
    model = Rol
    template_name = 'tickets/roluser_list.html'
    context_object_name = 'rol'

class UpdateRol(UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'tickets/roluser_update.html'
    success_url = reverse_lazy('listrol')

    def form_valid(self, form):
        messages.success(self.request, '¡Rol Actualizado con exito!')
        return super().form_valid(form)

class DeleteRol(DeleteView):
    model = Rol
    template_name = 'tickets/roluser_delete.html'
    context_object_name = 'rol'
    success_url = reverse_lazy('listrol')

    def form_valid(self, form):
        messages.success(self.request, '¡Rol Eliminado con exito!')
        return super().form_valid(form)
    
# ----------------------------------- # PROTOCOLOS

@method_decorator(login_required, name='dispatch')    
class CreateProtocolo(CreateView, ListView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'tickets/protocolo.html'
    success_url = reverse_lazy('protocolos')
    context_object_name = 'protocolos'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_valid(self, form):
        messages.success(self.request, '¡Protocolo Agregado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')    
class UpdateProtocolo(UpdateView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'tickets/protocolo_update.html'
    success_url = reverse_lazy('protocolos')

    def form_valid(self, form):
        messages.success(self.request, '¡Protocolo Actualizado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeleteProtocolo(DeleteView):
    model = Protocolo
    template_name = 'tickets/protocolo_delete.html'
    success_url = reverse_lazy('protocolos')
    context_object_name = 'protocolos'

    def form_valid(self, form):
        messages.success(self.request, '¡Protocolo Eliminado con exito!')
        return super().form_valid(form)

# ----------------------------------- # USUARIOS

@method_decorator(login_required, name='dispatch')
class CreateUsuario(UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'tickets/usercreate.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, '¡Usuario Registrado con exito!')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')    
class ListUsuario(ListView):
    model = Usuario
    template_name = 'tickets/userlist.html'
    context_object_name = 'usersys'

@method_decorator(login_required, name='dispatch')
class UpdateUsuario(UpdateView):
    model = Usuario
    form_class = UserUpdateForm
    template_name = 'tickets/userupdate.html'
    success_url = reverse_lazy('userlist')
    context_object_name = 'usuario'

    def form_valid(self, form):
        messages.success(self.request, '¡Usuario Actualizado con exito!')
        return super().form_valid(form)

    # def get_object(self, queryset=None):
    #     pk = self.kwargs.get('pk')
    #     return Usuario.objects.get(pk=pk)

@method_decorator(login_required, name='dispatch')    
class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'tickets/userdelete.html'
    success_url = reverse_lazy('userlist')
    context_object_name = 'usuario'

    def form_valid(self, form):
        messages.success(self.request, '¡Usuario Eliminado con exito!')
        return super().form_valid(form)

# ----------------------------------- # ESTADOS DE TICKETS

@method_decorator(login_required, name='dispatch')
class ListTicketState(ListView):
    model = TicketState
    form_class = TicketStateForm
    template_name = 'tickets/ticketstate.html'
    context_object_name = 'Estado'
    
@method_decorator(login_required, name='dispatch')
class CreateTicketState(UserPassesTestMixin, CreateView):
    model = TicketState
    form_class = TicketStateForm
    template_name = 'tickets/ticketstate_create.html'
    success_url = reverse_lazy('statelist')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']
    
    def form_valid(self, form):
        messages.success(self.request, '¡Estado Registrado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class UpdateTicketState(UserPassesTestMixin, UpdateView):
    model = TicketState
    form_class = TicketStateForm
    template_name = 'tickets/ticketstate_update.html'
    success_url = reverse_lazy('statelist')
    context_object_name = 'Estado'
    
    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Estado Actualizado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')    
class DeleteTicketState(UserPassesTestMixin, DeleteView):
    model = TicketState
    template_name = 'tickets/ticketstate_delete.html'
    success_url = reverse_lazy('statelist')
    context_object_name = 'Estado'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Estado Eliminado con exito!')
        return super().form_valid(form)

# ----------------------------------- # TICKETS DE ENTRADA

@method_decorator(login_required, name='dispatch')    
class CreateTicketE(CreateView, ListView):
    model = TicketE
    form_class = TicketEForm
    template_name = 'tickets/ticket_entrada.html'
    success_url = reverse_lazy('ticketE')
    context_object_name = 'TicketE'

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Entrada Creado con exito!')
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')    
class UpdateTicketE(UpdateView):
    model = TicketE
    form_class = TicketEForm # FORMULARIO TEMPORAL, REVISAR REQUERIMIENTOS
    template_name = 'tickets/tickete_update.html'
    success_url = reverse_lazy('ticketE')

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Entrada Editado con exito!')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')    
class CloseTicketE(UpdateView):
    model = TicketE
    form_class = TicketEStateForm
    template_name = 'tickets/tickete_close.html'
    success_url = reverse_lazy('ticketE')

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Entrada Cerrado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeleteTicketE(DeleteView):
    model = TicketE
    template_name = 'tickets/tickete_delete.html'
    success_url = reverse_lazy('ticketE')
    context_object_name = 'TicketE'

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de entrada Eliminado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DetailTicketE(DetailView):
    model = TicketE
    template_name = 'tickets/tickete_detail.html'
    context_object_name = 'TicketE'

# ----------------------------------- #

def custom_logout(request):
    logout(request)  
    return redirect('login') 