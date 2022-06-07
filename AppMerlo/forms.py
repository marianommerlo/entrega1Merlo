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
    first_name= forms.CharField(required= True, label= 'Nombre')
    last_name= forms.CharField(required= True, label= 'Apellido')
    descripcion= forms.CharField(required= False, label= 'Descripción')
    web= forms.URLField(required= False)
    password1= forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Confirmar Contraseña', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    #especificamos los campos del formulario
    email= forms.EmailField(required= False, label= 'Modificar Email')
    last_name= forms.CharField(required= False, label= 'Modificar Apellido')
    first_name= forms.CharField(required= False, label= 'Modificar Nombre')
    descripcion= forms.CharField(required= False, label= 'Descripción')
    web= forms.URLField(required= False)

    password1= forms.CharField(required= False, label= 'Modificar Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Confirmar Contraseña', widget= forms.PasswordInput)
    

    class Meta:
        model= User
        fields= ['email', 'password1', 'password2', 'last_name', 'first_name', 'web', 'descripcion']
        help_texts= {k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar= forms.ImageField(label= 'Avatar')