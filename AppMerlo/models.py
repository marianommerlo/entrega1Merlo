from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Broker(models.Model):
    empresa= models.CharField(max_length=50)
    telefono= models.IntegerField()
    email= models.EmailField(max_length=50)

    def __str__(self):
        return self.empresa

class Suscripcion(models.Model):
    plan= models.CharField(max_length=50)
    precio= models.IntegerField()
    periodicidad= models.CharField(max_length=50)

    def __str__(self):
        return self.plan +" ---> "+ self.periodicidad

class Perfil(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    descripcion= models.CharField(max_length=500)
    web= models.URLField()
    avatar= models.ImageField(upload_to= 'avatar/', blank= True)

    
class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)
