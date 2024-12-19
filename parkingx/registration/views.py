from django.forms import ValidationError
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from tickets.models import Usuario
from registration.form import ProfileForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import re

from django.contrib import messages

def validar_rut(rut):
    rut = rut.replace(".", "").upper()
    match = re.match(r"^(\d{1,8})[-]([0-9Kk])$", rut)

    if not match:
        raise ValidationError("El RUT tiene un formato incorrecto")
    return True

class ProfileView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'registration/profile.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Usuario
    form_class = ProfileForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user

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
        
        messages.success(self.request, '¡Perfil de Usuario Actualizado!')
        return super().form_valid(form)
   