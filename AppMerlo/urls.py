from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

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

    #Login/Logout/Registro
    path('login/', login_request, name= 'login'),
    path('logout/', LogoutView.as_view(template_name="AppMerlo/logout.html"), name= 'logout'),
]