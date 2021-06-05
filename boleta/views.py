from django.shortcuts import render
from .models import Boleta, Cliente, Producto
from .serializers import BoletaSerializer, ProductoSerializer, ClienteSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class ProductoApi(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class BoletaApi(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class ClienteApi(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@api_view(['GET'])
def cliente_detail_view(request,pk=None):
	if request.method == 'GET':
		cliente = Cliente.objects.filter(rut=pk).first()
		if cliente == None:
			return Response("No existe cliente.")
		else:
			cliente_serializer= ClienteSerializer(cliente)
			return Response(cliente_serializer.data)
'''
class ProductoApi(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        producto = Producto.objects.all()
        return producto

class BoletaApi(viewsets.ModelViewSet):
    serializer_class = BoletaSerializer
    def get_queryset(self):
        boleta = Boleta.objects.all()
        return boleta

class ClienteApi(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    def get_queryset(self):
        cliente = Cliente.objects.all()
        return cliente

    def create(self, request, *args, **kwargs):
        data = request.data
        new_cliente = Cliente.objects.create(rut=data['rut'],nombre_cl=data['nombre_cl'],direccion=data['direccion'],boletas=data['boletas'])
        new_cliente.save()

        for boleta in data["boletas"]:
            boleta_obj = Boleta.object.get(num_boleta=boleta["num_boleta"],productos=data['productos'])
            new_cliente.boletas.add(boleta_obj)

        serializer = ClienteSerializer(new_cliente)

        return Response(serializer.data)
'''
