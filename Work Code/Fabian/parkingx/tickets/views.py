from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.core.exceptions import ValidationError
import re

from django.contrib import messages
from datetime import datetime

from .models import Rol, Usuario, Protocolo, TicketEntrada, TicketState, TicketSalida
from .forms import RolForm, UsuarioForm, UserUpdateForm, ProtocoloForm, TicketEForm, TicketEUpdateForm, TicketStateForm, TicketEStateForm, TicketSForm, TicketSEditForm

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# ------------------------------ # Rut
def validar_rut(rut):
    # Eliminar puntos y convertir a mayúsculas
    rut = rut.replace(".", "").upper()
    
    # Comprobar que el formato del RUT sea correcto (xxxxxxx-X)
    match = re.match(r"^(\d{1,8})[-]([0-9Kk])$", rut)
    if not match:
        raise ValidationError("El RUT tiene un formato incorrecto")
    return True
# ----------------------------------- # HOME

@login_required
def Home(request):
    return render(request, 'tickets/base.html')

# ----------------------------------- # ROLES

@method_decorator(login_required, name='dispatch')
class CreateRol(UserPassesTestMixin, CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'tickets/roles/roluser_create.html'
    success_url = reverse_lazy('listrol')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Rol Agregado con exito!')
        return super().form_valid(form)
    
    
class ListRol(UserPassesTestMixin, ListView):
    model = Rol
    template_name = 'tickets/roles/roluser_list.html'
    context_object_name = 'rol'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

def FindRol(request):
    response = request.GET.get('find-rol')
    if response:
        roluser = Rol.objects.filter(name__icontains = response)
    else:
        roluser = Rol.objects.all()   
    return render(request, 'tickets/roles/rolser_find.html', {'rol':roluser, 'response':response})

class UpdateRol(UserPassesTestMixin, UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'tickets/roles/roluser_update.html'
    success_url = reverse_lazy('listrol')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Rol Actualizado con exito!')
        return super().form_valid(form)

class DeleteRol(UserPassesTestMixin, DeleteView):
    model = Rol
    template_name = 'tickets/roles/roluser_delete.html'
    context_object_name = 'rol'
    success_url = reverse_lazy('listrol')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Rol Eliminado con exito!')
        return super().form_valid(form)
    
# ----------------------------------- # PROTOCOLOS

@method_decorator(login_required, name='dispatch')    
class CreateProtocolo(UserPassesTestMixin, CreateView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'tickets/protocolos/protocolo.html'
    success_url = reverse_lazy('protocolos')
    context_object_name = 'protocolos'

    # Método para listar todos los protocolos
    def get_queryset(self):
        return Protocolo.objects.all()

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']
    
    def form_valid(self, form):
        
        rut = form.cleaned_data.get('rut')
        try:
            validar_rut(rut)
        except ValidationError as e:
            form.add_error('rut', str(e))
            return self.form_invalid(form)

        name = form.cleaned_data.get('name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', name):
            form.add_error('name', 'El nombre solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        last_name = form.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', last_name):
            form.add_error('last_name', 'El apellido solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        hora_ingreso = form.cleaned_data.get('hora_ingreso')
        if hora_ingreso and hora_ingreso >= datetime.now().time():
            form.add_error('hora_ingreso', 'La hora de ingreso debe ser anterior a la hora actual.')
            return self.form_invalid(form)
        
        hora_salida = form.cleaned_data.get('hora_salida')
        if hora_salida and hora_salida <= hora_ingreso:
            form.add_error('hora_salida', 'La hora de salida debe ser despues a la hora de ingreso.')
            return self.form_invalid(form)
        
        patente = form.cleaned_data.get('patente')
        if not re.match(r'^[A-Z]{4}\d{2}$', patente):
            form.add_error('patente', 'La patente debe tener 4 letras mayusculas seguidas de 2 números.')
            return self.form_invalid(form)

        messages.success(self.request, '¡Protocolo Agregado con exito!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Llamar al contexto original de CreateView
        context = super().get_context_data(**kwargs)
        
        # Añadir la lista de protocolos al contexto
        context['protocolos'] = self.get_queryset()  # Pasa los protocolos al contexto

        # Añadir el formulario de creación al contexto (en caso de POST, será el formulario inválido)
        if self.request.method != 'POST':
            context['form'] = self.get_form()

        return context

@method_decorator(login_required, name='dispatch')    
class UpdateProtocolo(UserPassesTestMixin, UpdateView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'tickets/protocolos/protocolo_update.html'
    success_url = reverse_lazy('protocolos')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):

        rut = form.cleaned_data.get('rut')
        try:
            validar_rut(rut)
        except ValidationError as e:
            form.add_error('rut', str(e))
            return self.form_invalid(form)

        name = form.cleaned_data.get('name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', name):
            form.add_error('name', 'El nombre solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        last_name = form.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', last_name):
            form.add_error('last_name', 'El apellido solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        hora_ingreso = form.cleaned_data.get('hora_ingreso')
        if hora_ingreso and hora_ingreso >= datetime.now().time():
            form.add_error('hora_ingreso', 'La hora de ingreso debe ser anterior a la hora actual.')
            return self.form_invalid(form)
        
        hora_salida = form.cleaned_data.get('hora_salida')
        if hora_salida and hora_salida <= hora_ingreso:
            form.add_error('hora_salida', 'La hora de salida debe ser despues a la hora de ingreso.')
            return self.form_invalid(form)
        
        patente = form.cleaned_data.get('patente')
        if not re.match(r'^[A-Z]{4}\d{2}$', patente):
            form.add_error('patente', 'La patente debe tener 4 letras mayusculas seguidas de 2 números.')
            return self.form_invalid(form)

        messages.success(self.request, '¡Protocolo Agregado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeleteProtocolo(UserPassesTestMixin, DeleteView):
    model = Protocolo
    template_name = 'tickets/protocolos/protocolo_delete.html'
    success_url = reverse_lazy('protocolos')
    context_object_name = 'protocolos'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Protocolo Eliminado con exito!')
        return super().form_valid(form)

# ----------------------------------- # USUARIOS

@method_decorator(login_required, name='dispatch')
class CreateUsuario(UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'tickets/usuarios/usercreate.html'
    success_url = reverse_lazy('userlist')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', username):
            form.add_error('username', 'El nombre de usuario solo puede contener letras y espacios.')
            return self.form_invalid(form)

        rut = form.cleaned_data.get('rut')
        try:
            validar_rut(rut)
        except ValidationError as e:
            form.add_error('rut', str(e))
            return self.form_invalid(form)

        name = form.cleaned_data.get('name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', name):
            form.add_error('name', 'El nombre solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        last_name = form.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', last_name):
            form.add_error('last_name', 'El apellido solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        user = form.save()
        messages.success(self.request, '¡Usuario Registrado con exito!')
        return super().form_valid(form)
    
    
    
@method_decorator(login_required, name='dispatch')    
class ListUsuario(UserPassesTestMixin, ListView):
    model = Usuario
    template_name = 'tickets/usuarios/userlist.html'
    context_object_name = 'usersys'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

@method_decorator(login_required, name='dispatch')
class UpdateUsuario(UserPassesTestMixin, UpdateView):
    model = Usuario
    form_class = UserUpdateForm
    template_name = 'tickets/usuarios/userupdate.html'
    success_url = reverse_lazy('userlist')
    context_object_name = 'usuario'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', username):
            form.add_error('username', 'El nombre de usuario solo puede contener letras y espacios.')
            return self.form_invalid(form)

        rut = form.cleaned_data.get('rut')
        try:
            validar_rut(rut)
        except ValidationError as e:
            form.add_error('rut', str(e))
            return self.form_invalid(form)

        name = form.cleaned_data.get('name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', name):
            form.add_error('name', 'El nombre solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        last_name = form.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚ\s]+$', last_name):
            form.add_error('last_name', 'El apellido solo puede contener letras y espacios.')
            return self.form_invalid(form)
        
        user = form.save()
        messages.success(self.request, '¡Usuario Registrado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')    
class DeleteUsuario(UserPassesTestMixin, DeleteView):
    model = Usuario
    template_name = 'tickets/usuarios/userdelete.html'
    success_url = reverse_lazy('userlist')
    context_object_name = 'usuario'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']

    def form_valid(self, form):
        messages.success(self.request, '¡Usuario Eliminado con exito!')
        return super().form_valid(form)

# ----------------------------------- # ESTADOS DE TICKETS

@method_decorator(login_required, name='dispatch')
class ListTicketState(UserPassesTestMixin, ListView):
    model = TicketState
    form_class = TicketStateForm
    template_name = 'tickets/estados/ticketstate.html'
    context_object_name = 'Estado'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador']
    
@method_decorator(login_required, name='dispatch')
class CreateTicketState(UserPassesTestMixin, CreateView):
    model = TicketState
    form_class = TicketStateForm
    template_name = 'tickets/estados/ticketstate_create.html'
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
    template_name = 'tickets/estados/ticketstate_update.html'
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
    template_name = 'tickets/estados/ticketstate_delete.html'
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
class CreateTicketE(View):
    template_name = 'tickets/tickets_entrada/ticket_entrada.html'

    def get(self, request):
        tickets = TicketEntrada.objects.all()
        form = TicketEForm()
        return render(request, self.template_name, {'form': form, 'TicketE': tickets})

    def post(self, request):
        form = TicketEForm(request.POST)
        tickets = TicketEntrada.objects.all()
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ticket de Entrada Creado con éxito!')       
            return render(request, self.template_name, {'form': form, 'TicketE': tickets})
        else:
            return render(request, self.template_name, {'form': form, 'TicketE': tickets})

@method_decorator(login_required, name='dispatch')    
class UpdateTicketE(UserPassesTestMixin, UpdateView):
    model = TicketEntrada
    form_class = TicketEUpdateForm # FORMULARIO TEMPORAL, REVISAR REQUERIMIENTOS
    template_name = 'tickets/tickets_entrada/tickete_update.html'
    success_url = reverse_lazy('ticketE')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador', 'Portero']

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Entrada Editado con exito!')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')    
class CloseTicketE(UpdateView):
    model = TicketEntrada
    form_class = TicketEStateForm
    template_name = 'tickets/tickets_entrada/tickete_close.html'
    success_url = reverse_lazy('ticketE')
    context_object_name = 'TicketE'

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Entrada Cerrado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeleteTicketE(UserPassesTestMixin, DeleteView):
    model = TicketEntrada
    template_name = 'tickets/tickets_entrada/tickete_delete.html'
    success_url = reverse_lazy('ticketE')
    context_object_name = 'TicketE'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador', 'Portero']

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Entrada Eliminado con exito!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DetailTicketE(DetailView):
    model = TicketEntrada
    template_name = 'tickets/tickets_entrada/tickete_detail.html'
    context_object_name = 'TicketE'

# ----------------------------------- # TICKETS DE SALIDA

@method_decorator(login_required, name='dispatch')
class TicketSView(UserPassesTestMixin, View):
    template_name = 'tickets/tickets_salida/ticketsalida.html'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador', 'Cajero']

    def get(self, request):
        form = TicketSForm
        tickets = TicketSalida.objects.all()
        return render(request, self.template_name, {'form': form,'TicketS': tickets})

    def post(self, request):
        form = TicketSForm(request.POST)
        if form.is_valid():
            patente = form.cleaned_data.get('patente')
            ticket_e = TicketEntrada.objects.filter(patente=patente).first()

            if not ticket_e:
                messages.error(request, 'No se encontró un ticket de entrada con la patente ingresada.')

            elif ticket_e.state.name != 'Cerrado':
                messages.error(request, 'El ticket de entrada no está cerrado.')
                print(ticket_e)

            else:
                exit_datetime = datetime.combine(datetime.today(), datetime.now().time().replace(second=0, microsecond=0))
                entrace_datetime = datetime.combine(ticket_e.date, ticket_e.entrace_time)
                raw_price = ((exit_datetime - entrace_datetime).total_seconds() // 60) * 20
                Price = (raw_price // 20) * 20

                ticket_s = TicketSalida(
                    date = ticket_e.date,
                    entrace_time = ticket_e.entrace_time,
                    patente = ticket_e.patente,
                    price = ticket_e.price,
                    exit_time = exit_datetime.time(),
                    min_lapsed = (exit_datetime - entrace_datetime).total_seconds() // 60, 
                    total = Price
                )
            
                ticket_s.save()
                messages.success(request, '¡Ticket de Salida Creado con exito!')   
            return self.get(request)
        
        else:
            tickets = TicketSalida.objects.all()
            return render(request, self.template_name, {'form': form,'TicketS': tickets})
        
@method_decorator(login_required, name='dispatch')    
class UpdateTicketS(UserPassesTestMixin, UpdateView):
    model = TicketSalida
    form_class = TicketSEditForm # FORMULARIO TEMPORAL, REVISAR REQUERIMIENTOS
    template_name = 'tickets/tickets_salida/ticketsalida_update.html'
    success_url = reverse_lazy('ticketS')

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador', 'Cajero']

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Salida Editado con exito!')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class DeleteTicketS(UserPassesTestMixin, DeleteView):
    model = TicketSalida
    template_name = 'tickets/tickets_salida/ticketsalida_delete.html'
    success_url = reverse_lazy('ticketS')
    context_object_name = 'TicketS'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador', 'Cajero']

    def form_valid(self, form):
        messages.success(self.request, '¡Ticket de Salida Eliminado con exito!')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class DetailTicketS(UserPassesTestMixin, DetailView):
    model = TicketSalida
    template_name = 'tickets/tickets_salida/ticketsalida_detail.html'
    context_object_name = 'TicketS'

    def test_func(self):
        rol = self.request.user.rol.name
        return rol in ['root', 'Administrador', 'Cajero']

# ----------------------------------- #

def custom_logout(request):
    logout(request)  
    return redirect('login') 