from django import forms
#pip install rut
#from rut import validate_rut  # Si usas la librería `rut`
from .models import Usuario, Rol, Protocolo, TicketEntrada, TicketState, TicketSalida
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'name', 'last_name', 'rut', 'email', 'rol', 'avatar','password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'rut': 'RUT',
            'email': 'Correo electrónico',
            'rol': 'Rol de Usuario',
            'avatar':'Foto de Usuario',
            'password1':'Contraseña',
            'password2':'Confirmar Contraseña'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'required': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'required': ''}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'required': ''}),
            'rut': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':9, 'maxlength':10, 'required': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-crud'}),
            'rol': forms.Select(attrs={'class': 'form-control form-crud'}),
            'avatar':forms.ClearableFileInput(attrs={'class': 'form-control form-crud'}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control form-crud'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control form-crud'})
        }

        # def clean_rut(self):
        #     rut = self.cleaned_data.get('rut')
            
        #     # Validar el formato del RUT y el dígito verificador
        #     try:
        #         validate_rut(rut)
        #     except ValueError:
        #         raise forms.ValidationError("El RUT ingresado no es válido.")
            
        #     # Verificar si el RUT ya está registrado en la base de datos
        #     if Usuario.objects.filter(rut=rut).exists():
        #         raise forms.ValidationError("El RUT ya está registrado.")
            
        #     return rut
    

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre del Rol',
            'description': 'Descripción'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2, 'maxlength':45, 'required': ''}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-2', 'rows': 3, 'minlength':2, 'required': ''}),
        }

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'name', 'last_name', 'rut', 'email', 'rol', 'avatar']
        labels = {
            'username': 'Nombre de Usuario',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'rut': 'RUT',
            'email': 'Correo electrónico',
            'rol': 'Rol de Usuario',
            'avatar':'Foto de Usuario'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'maxlength':45, 'required': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'maxlength':45, 'required': ''}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'maxlength':45, 'required': ''}),
            'rut': forms.TextInput(attrs={'class': 'form-control form-crud', 'minlength':9, 'maxlength':10, 'required': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-crud', 'minlength':2, 'maxlength':45, 'required': ''}),
            'rol': forms.Select(attrs={'class': 'form-control form-crud'}),
            'avatar':forms.ClearableFileInput(attrs={'class': 'form-control form-crud'})

        }

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
            'name': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2, 'maxlength':45, 'required': ''}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2, 'maxlength':45, 'required': ''}),
            'rut': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':9, 'maxlength':10, 'required': ''}),
            'number': forms.NumberInput(attrs={'class': 'form-control mt-2', 'minlength':9, 'maxlength':9, 'required': ''}),
            'patente': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':6, 'required': ''}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mt-2'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mt-2'}),
            'date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control mt-2'}),
            'description': forms.TextInput(attrs={'class': 'form-control mt-2', 'minlength':2, 'required': ''}),
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
