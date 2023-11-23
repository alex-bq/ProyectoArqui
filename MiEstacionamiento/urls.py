from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("arrendar/arrendar/", views.guardar_arriendo, name="arrendar_arrendar"),
    path("arrendar/", views.arrendar, name="arrendar"),
]
