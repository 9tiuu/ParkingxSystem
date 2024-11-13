from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Rol, Usuario, Protocolo
from .forms import RolForm, UsuarioForm, UserUpdateForm, ProtocoloForm

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# ----------------------------------- #

@login_required
def Home(request):
    return render(request, 'tickets/base.html')

# ----------------------------------- #

@method_decorator(login_required, name='dispatch')
class CreateRol(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'tickets/createrol.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    
# ----------------------------------- #

@method_decorator(login_required, name='dispatch')    
class CreateProtocolo(CreateView, ListView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'tickets/protocolo.html'
    success_url = reverse_lazy('protocolo')
    context_object_name = 'protocolos'

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')    
class UpdateProtocolo(UpdateView):
    model = Protocolo
    form_class = ProtocoloForm
    template_name = 'tickets/protocolo_update.html'
    success_url = reverse_lazy('protocolo')

@method_decorator(login_required, name='dispatch')
class DeleteProtocolo(DeleteView):
    model = Protocolo
    template_name = 'tickets/protocolo_delete.html'
    success_url = reverse_lazy('protocolo')
    context_object_name = 'protocolos'

# ----------------------------------- #

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
    success_url = reverse_lazy('home')
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Usuario.objects.get(pk=pk)

@method_decorator(login_required, name='dispatch')    
class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'tickets/userdelete.html'
    success_url = reverse_lazy('userlist')
    context_object_name = 'usuario'

# ----------------------------------- #

def custom_logout(request):
    logout(request)  
    return redirect('login') 