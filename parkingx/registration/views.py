from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from tickets.models import Usuario
from registration.form import ProfileForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib import messages

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
        messages.success(self.request, '¡Perfil de Usuario Actualizado!')
        return super().form_valid(form)
   