from django.contrib import admin
from django.urls import path
from . import views

# login
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("arrendar/arrendar/", views.guardar_arriendo, name="arrendar_arrendar"),
    path("arrendar/", views.arrendar, name="arrendar"),
    path("login/", LoginView.as_view(template_name="index.html"), name="login"),
]
