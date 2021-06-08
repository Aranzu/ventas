from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from boleta.views import (
	cliente_detail_view, boleta_detail_view
	)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("Boleta",views.BoletaApi, basename="boleta")
router.register("Producto",views.ProductoApi, basename="producto")
router.register("Cliente",views.ClienteApi, basename="cliente")

urlpatterns = [
    path('',include(router.urls)),
    path('cl/<int:pk>/', cliente_detail_view, name= "cliente_api"),
    path('boleta/<int:pk>/', boleta_detail_view, name= "boleta_api"),
]
