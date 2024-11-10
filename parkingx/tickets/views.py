from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Rol, Usuario
from .forms import RolForm, UsuarioForm, UserUpdateForm

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# ----------------------------------- #

@login_required
def Home(request):
    return render(request, 'tickets/base.html')

# ----------------------------------- #

class CreateRol(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'tickets/createrol.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    
# ----------------------------------- #
    
class CreateUsuario(UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'tickets/usercreate.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.rol.name == 'root'
    
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
    
class ListUsuario(ListView):
    model = Usuario
    template_name = 'tickets/userlist.html'
    context_object_name = 'usersys'

class UpdateUsuario(UpdateView):
    model = Usuario
    form_class = UserUpdateForm
    template_name = 'tickets/userupdate.html'
    success_url = reverse_lazy('home')
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Usuario.objects.get(pk=pk)
    
class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'tickets/userdelete.html'
    success_url = reverse_lazy('userlist')
    context_object_name = 'usuario'

# ----------------------------------- #

def custom_logout(request):
    logout(request)  
    return redirect('login') 