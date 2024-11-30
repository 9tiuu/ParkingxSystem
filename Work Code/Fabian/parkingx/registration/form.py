from django import forms
from tickets.models import Usuario

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}), help_text="")
    name = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    last_name = forms.CharField(max_length=50, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    rut = forms.CharField(max_length=10, label='RUT', widget=forms.TextInput(attrs={'class': 'form-control form-crud'}))
    email = forms.EmailField(max_length=254, label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control form-crud'}))
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control form-crud'}))

    class Meta:
        model = Usuario
        fields = ['username', 'name', 'last_name', 'rut', 'email', 'avatar']