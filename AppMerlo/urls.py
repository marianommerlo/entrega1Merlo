from django.urls import path
from .views import * 

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('clientes/', clientes, name= 'clientes'),
    path('brokers/', brokers, name= 'brokers'),
    path('suscripciones/', suscripciones, name= 'suscripciones'),
    #path('clientesFormulario/', ClienteFormulario, name= 'clientesFormulario'),
    #path('brokersFormulario/', BrokerFormulario, name= 'brokersFormulario'),
    #path('suscripcionesFormulario/', SuscripcionFormulario, name= 'suscripcionesFormulario'),
    path('busquedaCliente/', busquedaCliente, name= 'busquedaCliente'),
    path('buscar/', buscar, name= 'buscar'),
]