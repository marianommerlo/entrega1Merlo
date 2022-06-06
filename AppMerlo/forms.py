from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()

class BrokerFormulario(forms.Form):
    empresa= forms.CharField(max_length=50)
    telefono= forms.IntegerField()
    email= forms.EmailField()

class SuscripcionFormulario(forms.Form):
    plan= forms.CharField(max_length=50)
    precio= forms.IntegerField()
    periodicidad= forms.CharField(max_length=50)


class UserRegistrationForm(UserCreationForm):
    #especificamos los campos del formulario
    email= forms.EmailField(required= True)
    password1= forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Confirmar Contraseña', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields} #Para que no se vean las ayudas para crear contraseña