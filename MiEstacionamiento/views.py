from django.shortcuts import render
from .models import *
from django import forms
from .forms import ClienteForm
from django.contrib import messages
from datetime import datetime
from .models import Vehiculo

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

#login
from django.contrib.auth.views import LoginView

# Create your views here.


def index(request):
    lista_arriendos = arriendoWardado.objects.all()
    context = {"lista_arriendos": lista_arriendos}
    return render(request, "index.html", context)

def clientes(request):
    lista_clientes = Cliente.objects.all()
    context = {"lista_clientes": lista_clientes}
    return render(request, "index.html", context)

def registro(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrado exitosamente.")
    else:
        form = ClienteForm()
    return render(request, "registro.html", {"form": form})


def guardar_arriendo(request):
    if request.method == "POST":
        hora_inic = request.POST.get("hora_inic")
        hora_fin = request.POST.get("hora_fin")
        patente = request.POST.get("patente")
        estatus = request.POST.get("estatus")

        # Corrige el nombre del modelo a Arriendo
        arriendo = arriendoWardado(
            hora_inic=hora_inic, hora_fin=hora_fin, patente=patente, estatus=estatus
        )
        arriendo.save()
        messages.success(request, "Arriendo guardado exitosamente.")

        return redirect("index")  # Redirige a la página de inicio

    return render(request, "index.html")


def arrendar(request):
    return render(request, "arrendar.html")


def login(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']
        user = authenticate(request, correo=correo, password=password)
        if user is not None:
            login(request, user)
            nombre_usuario = user.nombre  # Obtén el nombre del usuario autenticado
            return render(request, 'index.html', {'correo': correo})
        else:
            error_message = 'Datos incorrectos o inexistentes. Inténtalo de nuevo.'
            return render(request, 'index.html', {'error_message': error_message})
    else:
        return render(request, 'index.html')