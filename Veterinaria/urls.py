from django.urls import path
from .views import index,registro,registrar_clinica,listar_clinica

urlpatterns = [
    path('',index, name="index"),
    path('registro/',registro, name="registro"),
    path('registrar_clinica/',registrar_clinica, name="registrar_clinica"),
    path('listar_clinica/',listar_clinica, name="listar_clinica"),
]