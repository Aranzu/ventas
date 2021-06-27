from rest_framework import serializers
from django.db.models import Sum, Avg
from .models import Producto, Cliente, Boleta, ItemProducto

# Serializers define the API representation.

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('rut','nombre_cl','num_telf','email','direccion','boletas')
        depth = 4

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ('num_boleta','created_at','itemProductos')
        depth = 3

class ItemProductoSerializer(serializers.ModelSerializer):
    boletas = BoletaSerializer(many=True, read_only=True)
    class Meta:
        model = ItemProducto
        fields = ("id_item",'cantidad','productos','boletas')
        depth = 2

class ProductoSerializer(serializers.ModelSerializer):
    items = ItemProductoSerializer(many=True, read_only=True)
    class Meta:
        model = Producto
        fields = ("id_prod",'nombre_pro','precio','items')

