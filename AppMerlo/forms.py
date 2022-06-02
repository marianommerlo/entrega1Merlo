from django import forms

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