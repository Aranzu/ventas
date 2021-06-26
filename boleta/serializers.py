from rest_framework import serializers
from django.db.models import Sum, Avg
from .models import Producto, Cliente, Boleta, ItemProducto
from django.db.models import Sum
from django.db.models import Count

# Serializers define the API representation.

class ItemProductoSerializer(serializers.ModelSerializer):
    total_item = serializers.IntegerField()
    class Meta:
        model = ItemProducto
        fields = ("id_item",'cantidad','total_item')
        depth = 2

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ('num_boleta','created_at','ItemProductos')
        depth = 3

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('rut','nombre_cl','num_telf','email','direccion','boletas')
        depth = 4

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id_prod",'nombre_pro','precio')

