from django.shortcuts import render, redirect
from .models import *

#from .forms import ClienteForm
from django.contrib import messages
from datetime import datetime
from .models import Vehiculo

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
#registro
from django.contrib.auth.models import User
from .forms import RegistroForm

#login
from .forms import LoginForm

#cerrar sesión 
from django.contrib.auth import logout



# Create your views here.


def index(request):
    lista_arriendos = arriendoWardado.objects.all()
    context = {"lista_arriendos": lista_arriendos}
    return render(request, "index.html", context)


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            messages.success(request, "Registrado exitosamente.")
            return redirect('index')  # Redirige al usuario a la página de inicio de sesión después del registro
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


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


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige al usuario a la página de inicio después del inicio de sesión
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # Reemplaza 'nombre_de_la_vista' con el nombre de la vista a la que deseas redirigir después de cerrar sesión 