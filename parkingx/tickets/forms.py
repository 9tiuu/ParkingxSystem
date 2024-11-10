from django import forms
from .models import Usuario, Rol
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}), help_text="")
    name = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    last_name = forms.CharField(max_length=50, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    rut = forms.CharField(max_length=10, label='RUT', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    email = forms.EmailField(max_length=254, label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control form-crud'}))
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-crud'}))
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control form-crud'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-crud'}), help_text="")
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-crud'}), help_text="")

    class Meta:
        model = Usuario
        fields = ['username', 'name', 'last_name', 'rut', 'email', 'rol', 'avatar']

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre del Rol',
            'description': 'Descripción del Rol'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}), help_text="")
    name = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    last_name = forms.CharField(max_length=50, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    rut = forms.CharField(max_length=10, label='RUT', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    email = forms.EmailField(max_length=254, label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control form-crud'}))
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-crud'}))
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control form-crud'}))

    class Meta:
        model = Usuario
        fields = ['username', 'name', 'last_name', 'rut', 'email', 'rol', 'avatar']
