from django.urls import path
from .views import index
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from Veterinaria.views import *
from .views import index,registro,registrar_clinica,listar_clinica

urlpatterns = [
    path('',index, name="index"),
    path('registro/',registro, name="registro"),
    path('registrar_clinica/',registrar_clinica, name="registrar_clinica"),
    path('listar_clinica/',listar_clinica, name="listar_clinica"),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]