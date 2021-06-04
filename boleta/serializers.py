from rest_framework import serializers
from django.utils import timezone
from .models import Producto, Cliente, Boleta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre_pro','precio','stock']

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ['num_boleta','created_at','total','productos']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut','nombre_cl','direccion','boletas']
        depth = 1


