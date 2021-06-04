from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    nombre_pro = models.CharField(max_length=100, primary_key=True)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre_pro

class Boleta(models.Model):
    num_boleta = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.num_boleta

class Cliente(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    nombre_cl = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    boletas = models.ManyToManyField(Boleta)

    def __str__(self):
        return self.rut