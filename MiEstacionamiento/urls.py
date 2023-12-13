from django.contrib import admin
from django.urls import path
from . import views

# login
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("guardar_arriendo/", views.guardar_arriendo, name="guardar_arriendo"),
    path("arrendar/", views.arrendar, name="arrendar"),
<<<<<<< HEAD
    path("login/", views.login_view, name="login"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
=======
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path("index/", views.index, name="index"),
    path("guardar_estacionamiento/", views.guardar_estacionamiento, name="guardar_estacionamiento"),
>>>>>>> origin/main
]
