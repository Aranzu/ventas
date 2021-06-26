from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .serializers import ProductoSerializer, BoletaSerializer, ClienteSerializer, ItemProductoSerializer
from .models import Producto, Cliente, Boleta, ItemProducto
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models import Count
# ViewSets define the view behavior.

class ProductoApi(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class BoletaApi(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class ClienteApi(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ItemProductoApi(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = ItemProducto.objects.all()
    serializer_class = ItemProductoSerializer

    def get_queryset(self):
        return ItemProducto.objects.annotate(
            total_item = (Sum('productos__precio') * Sum('cantidad'))
        )

@api_view(['GET'])
def cliente_detail_view(request,pk=None):
	if request.method == 'GET':
		cliente = Cliente.objects.filter(rut=pk).first()
		if cliente == None:
			return Response("No existe cliente.")
		else:
			cliente_serializer= ClienteSerializer(cliente)
			return Response(cliente_serializer.data)

@api_view(['GET'])
def boleta_detail_view(request,pk=None):
	if request.method == 'GET':
		boleta = Boleta.objects.filter(num_boleta=pk).first()
		if boleta == None:
			return Response("No existe la boleta ingresada.")
		else:
			boleta_serializer= BoletaSerializer(boleta)
			return Response(boleta_serializer.data)
