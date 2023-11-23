from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('guardar_arriendo/', views.guardar_arriendo, name='guardar_arriendo'),
]