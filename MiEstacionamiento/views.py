from django.shortcuts import render, redirect
from .models import *

# from .forms import ClienteForm
from django.contrib import messages
from datetime import datetime
from .models import Vehiculo
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# registro
from django.contrib.auth.models import User
from .forms import RegistroForm


# cerrar sesión
from django.contrib.auth import logout
from .models import arriendoWardado
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


def index(request):
    lista_arriendos = arriendoWardado.objects.all()
    context = {"lista_arriendos": lista_arriendos}
    return render(request, "index.html", context)


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            rol = request.POST.get("rol")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )

            messages.success(request, "Registrado exitosamente.")
            return redirect("index")  # Redirige a la página de inicio
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})


@login_required
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


def login_view(request):
    if request.method == "POST":
        print("entre al post")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("entre al if form.is_valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"Usuario autenticado: {user}")
                login(request, user)
                print("Redirigiendo al usuario a la página principal")
                return redirect(
                    "/"
                )  # Cambia 'index' por la URL a la que deseas redirigir al usuario después del inicio de sesión
            else:
                print("Autenticación fallida")
                pass  # Puedes manejar esto según tus necesidades
    else:
        print("estoi en el else qlo")
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("/")
