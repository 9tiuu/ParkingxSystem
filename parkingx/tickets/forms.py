from django import forms
from .models import Usuario, Rol, Protocolo, TicketEntrada, TicketState, TicketSalida
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
            'description': 'Descripción'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-2', 'rows': 3}),
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

class ProtocoloForm(forms.ModelForm):
    
    class Meta:
        model = Protocolo
        fields = ['name', 'last_name', 'rut', 'number', 'patente', 'hora_ingreso', 'hora_salida', 'date', 'description']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'rut': 'RUT',
            'number': 'Número telefónico',
            'patente': 'Patente Vehicular',
            'hora_ingreso': 'Hora de Ingreso',
            'hora_salida': 'Hora de Salida',
            'date': 'Fecha',
            'description': 'Descripción'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2}),
            'rut': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':10}),
            'number': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':9}),
            'patente': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':6}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mt-2'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mt-2'}),
            'date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control mt-2'}),
            'description': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2}),
        }
        
class TicketEForm(forms.ModelForm): # MODIFICAR ------
    class Meta:
        model = TicketEntrada
        fields = ['patente', 'date', 'entrace_time']
        labels = {
            'patente': 'Patente vehicular',
            'date': 'Fecha',
            'entrace_time': 'Hr Ingreso'
        }
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':6, 'maxlength':6}),
            'date': forms.TextInput(attrs={'type':'date', 'id':'date-form' ,'class': 'form-control mt-2'}),
            'entrace_time': forms.TimeInput(attrs={'type':'time',  'id':'hour-form' ,'class': 'form-control mt-2'})
        }

class TicketEUpdateForm(forms.ModelForm): # MODIFICAR ------
    class Meta:
        model = TicketEntrada
        fields = ['patente','date','entrace_time', 'state']
        labels = {
            'patente': 'Patente',
            'date': 'Fecha',
            'entrace_time': 'Hr Ingreso',
            'state': 'Estado (Temporal)'
        }
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':6, 'maxlength':6}),
            'date': forms.TextInput(attrs={'type':'date', 'class': 'form-control mt-2'}),
            'entrace_time': forms.TimeInput(attrs={'type':'time', 'class': 'form-control mt-2'}),
            'state': forms.Select(attrs={'class':'form-control mt-2'})
        }

class TicketEStateForm(forms.ModelForm): # MODIFICAR ------
    class Meta:
        model = TicketEntrada
        fields = ['state']
        labels = {
            'state': 'Estado'
        }
        widgets = {
            'state': forms.Select(attrs={'class':'form-control mt-2'})
        }

class TicketStateForm(forms.ModelForm):  
    class Meta:
        model = TicketState
        fields = ['name', 'description']
        labels = {
            'name':'Nombre de Estado',
            'description':'Descripción'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mt-2'}),
            'description':forms.Textarea(attrs={'class':'form-control mt-2'})
        }

class TicketSForm(forms.ModelForm): # MODIFICAR ------
    class Meta:
        model = TicketSalida
        fields = ['patente']
        labels = {
            'patente': 'Patente vehicular'
        }
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':6, 'maxlength':6})
        }

class TicketSEditForm(forms.ModelForm): # MODIFICAR ------
    class Meta:
        model = TicketSalida
        fields = ['date', 'entrace_time','exit_time']
        labels = {
            'date': 'Fecha',
            'entrace_time' : 'Hr Ingreso',
            'exit_time': 'Hr Salida'
        }
        widgets = {
            'date': forms.TextInput(attrs={'type':'date','class': 'form-control mt-2'}),
            'entrace_time': forms.TimeInput(attrs={'type':'time','class': 'form-control mt-2'}),
            'exit_time': forms.TimeInput(attrs={'type':'time', 'class': 'form-control mt-2'})
        }
