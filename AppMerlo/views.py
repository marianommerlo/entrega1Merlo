import email
from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMerlo.forms import *

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