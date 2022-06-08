from dataclasses import fields
from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMerlo.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        avatar= Avatar.objects.filter(user= request.user)
        return render(request, 'AppMerlo/inicio.html', {'url': avatar[0].avatar.url})
    else:
        return render(request, template_name='AppMerlo/inicio.html')

#Formularios
@login_required
def clientes(request):

    if request.method == 'POST':
        miFormulario= ClienteFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            cliente= Cliente(nombre= informacion['nombre'], apellido= informacion['apellido'], email= informacion['email'])
            cliente.save()
            return render(request, 'AppMerlo/inicio.html')

    else:
        miFormulario= ClienteFormulario()
    
    return render(request, 'AppMerlo/clientes.html', {'formulario': miFormulario})

    #if request.method == 'POST':
    #    miFormulario= clienteFormulario(request.POST)
        
    #    if miFormulario.is_valid():
    #        informacion= miFormulario.cleaned_data
    #        cliente= Cliente(nombre=informacion['nombre'], apellido= informacion['apellido'], email= informacion['email'])
    #        cliente.save()
    #        return render(request, 'AppMerlo/inicio.html')

    #else:
    #    miFormulario= ClienteFormulario()
    
    #return render(request, 'AppMerlo/clientesFormulario.html', {'formulario': miFormulario})

@login_required
def brokers(request):
    if request.method == 'POST':
        miFormulario= BrokerFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            broker= Broker(empresa= informacion['empresa'], telefono= informacion['telefono'], email= informacion['email'])
            broker.save()
            return render(request, 'AppMerlo/inicio.html')

    else:
        miFormulario= BrokerFormulario()
    
    return render(request, 'AppMerlo/brokers.html', {'formulario': miFormulario})

    #if request.method == 'POST':
    #    miFormulario= brokerFormulario(request.POST)
        
    #    if miFormulario.is_valid():
    #        informacion= miFormulario.cleaned_data
    #        broker= Broker(empresa=informacion['empresa'], telefono= informacion['telefono'], email= informacion['email'])
    #        broker.save()
    #        return render(request, 'AppMerlo/inicio.html')

    #else:
    #    miFormulario= BrokerFormulario()
    
    #return render(request, 'AppMerlo/brokersFormulario.html', {'formulario': miFormulario})

@login_required
def suscripciones(request):

    if request.method == 'POST':
        miFormulario= SuscripcionFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            suscripcion= Suscripcion(plan= informacion['plan'], precio= informacion['precio'], periodicidad= informacion['periodicidad'])
            suscripcion.save()
            return render(request, 'AppMerlo/inicio.html')

    else:
        miFormulario= SuscripcionFormulario()
    
    return render(request, 'AppMerlo/suscripciones.html', {'formulario': miFormulario})

    #if request.method == 'POST':
    #    miFormulario= suscripcionFormulario(request.POST)
        
    #    if miFormulario.is_valid():
    #        informacion= miFormulario.cleaned_data
    #        suscripcion= Suscripcion(plan=informacion['plan'], precio= informacion['precio'], periodicidad= informacion['periodicidad'])
    #        suscripcion.save()
    #        return render(request, 'AppMerlo/inicio.html')

    #else:
    #    miFormulario= SuscripcionFormulario()
    
    #return render(request, 'AppMerlo/suscripcionesFormulario.html', {'formulario': miFormulario})


#Búsquedas

def busquedaCliente(request):
    return render(request, 'AppMerlo/busquedaCliente.html')

def buscar(request):
    if request.GET['apellido']:
        apellido= request.GET['apellido']
        clientes= Cliente.objects.filter(apellido= apellido)

        return render(request, 'AppMerlo/resultadosBusqueda.html', {'clientes': clientes, 'apellido': apellido})

    else:
        respuesta= "No se ingreso ningún apellido"
        return render(request, 'AppMerlo/resultadosBusqueda.html', {'respuesta': respuesta})


#LOGIN/REGISTER---------------------------------------------------------------------------------------------

def login_request(request):

    if request.method == "POST":
        formulario= AuthenticationForm(request, data= request.POST)

        if formulario.is_valid():
            usuario= formulario.cleaned_data.get('username')
            clave= formulario.cleaned_data.get('password')
            user= authenticate(username= usuario, password= clave)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppMerlo/inicio.html', {'mensaje': f'Bienvenido al Sistema {usuario}'})
            
        else:
            return render(request, 'AppMerlo/login.html', {'formulario': formulario, 'mensaje': 'Usuario incorrecto, vuelva a loguearse'})
    
    else:
        formulario= AuthenticationForm()
        return render(request, 'AppMerlo/login.html', {'formulario': formulario})


def registro(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            formulario.save()

            return render(request, 'AppMerlo/inicio.html', {'mensaje': f'Usuario {username} creado satisfactoriamente'})

        else:
            return render(request, 'AppMerlo/inicio.html', {'mensaje': 'No se pudo crear el usuario, intente nuevamente'})

    else:
        formulario= UserRegistrationForm()
        return render(request, 'AppMerlo/registro.html', {'formulario': formulario})



#PERFIL-------------------------------------------------------------------------------------------

class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'AppMerlo/perfil_listar.html'
#No lo estaría necesitando

class PerfilDetalle(LoginRequiredMixin, DetailView):
    model= Perfil
    template_name= 'AppMerlo/perfil_detalle.html'

class PerfilEdicion(UpdateView):
    model= Perfil
    success_url= reverse_lazy('perfil_listar')
    fields= ['nombre', 'apellido', 'email', 'web', 'descripcion', 'avatar']

class PerfilEliminacion(DeleteView):
    model= Perfil
    success_url= reverse_lazy('perfil_listar')
    fields= ['user', 'nombre', 'apellido', 'email']

@login_required
def editarPerfil(request):
    usuario= request.user

    if request.method == 'POST':
        formulario= UserEditForm(request.POST, instance= usuario)

        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()

            return render(request, 'AppMerlo/perfil_detalle.html', {'usuario': usuario, 'mensaje': f'Perfil de {usuario} editado satisfactoriamente'})

    else:
        formulario= UserEditForm(instance= usuario)
        
    return render(request, 'AppMerlo/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})


def agregarAvatar(request):
    user= User.objects.get(username= request.user)
    if request.method == 'POST':
        formulario= AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
          
                
            avatar= Avatar(user= user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AppMerlo/perfil_detalle.html', {'usuario': user, 'mensaje': f'Avatar de {user} agregado satisfactoriamente'})

    else:
        formulario= AvatarForm()
    
    return render(request, 'AppMerlo/agregarAvatar.html', {'formulario': formulario, 'usuario': user})
