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

# Create your views here.

def inicio(request):
    return render(request, 'AppMerlo/inicio.html')

#Formularios
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


#LOGIN/LOGOUT/REGISTER---------------------------------------------------------------------------------------------

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
            return render(request, 'AppMerlo/login.html', {'formulario': formulario, 'mensaje': 'Formulario inválido, vuelva a loguearse'})
    
    else:
        formulario= AuthenticationForm()
        return render(request, 'AppMerlo/login.html', {'formulario': formulario})


def registro(request):
    if request.method == "POST":
        formulario= UserRegistrationForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return render(request, 'AppMerlo/login.html', {f'mensaje': 'Usuario {username} creado correctamente'})