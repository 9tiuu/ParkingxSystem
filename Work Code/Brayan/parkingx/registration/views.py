from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from tickets.models import Usuario
from tickets.forms import UserUpdateForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'registration/profile.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    pass
    # USAR MISMO FORMULARIO DE ACTUALIZACION DE USUARIOS = UserUpdateForm
   