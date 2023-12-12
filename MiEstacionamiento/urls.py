from django.contrib import admin
from django.urls import path
from . import views

# login
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path('guardar_arriendo/', views.guardar_arriendo, name='guardar_arriendo'),
    path("arrendar/", views.arrendar, name="arrendar"),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
]
