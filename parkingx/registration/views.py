from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from tickets.models import Usuario
from tickets.forms import UsuarioForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView 
from django.contrib.auth.views import LoginView

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'registration/profile.html'
    form_class = UsuarioForm
    context_object_name = 'usuario'

    def get_object(self):
        # Esto asegura que el usuario solo puede actualizar su propio perfil
        return self.request.user

    def get_success_url(self):
        # Redirigir al perfil después de una actualización exitosa
        return reverse_lazy('profile')
