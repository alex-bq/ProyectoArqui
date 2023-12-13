from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# from .forms import ClienteForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# registro
from django.contrib.auth.models import User
from .forms import RegistroForm


# cerrar sesión
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, TarjetaForm

# Create your views here.


def index(request):
    lista_arriendos = Arriendo.objects.all()
    context = {"lista_arriendos": lista_arriendos}
    estacionamientos = Estacionamiento.objects.all()
    return render(request, "index.html", {"estacionamientos": estacionamientos})


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
        arriendo = arriendoWardado(
            hora_inic=hora_inic, hora_fin=hora_fin, patente=patente
        )
        arriendo.save()
        messages.success(request, "Arriendo guardado exitosamente.")

        return redirect("index")  # Redirige a la página de inicio

    return render(request, "index.html")


def guardar_estacionamiento(request):
    if request.method == "POST":
        direccion = request.POST.get("direccion")
        valorMinu = request.POST.get("valorMinu")
        user_id = request.user.id

        print("Valor ingresado en 'direccion':", direccion)
        print("Valor ingresado en 'valorMinu':", valorMinu)
        # Validar que valorMinu sea un número
        try:
            valorMinu = int(valorMinu)
        except ValueError:
            # Manejar el error de valor no numérico
            messages.error(request, "El valor por minuto debe ser un número válido.")
            return redirect("index")

        estacionamiento = Estacionamiento(
            valorMinu=valorMinu, direccion=direccion, user_id=user_id
        )
        estacionamiento.save()
        messages.success(request, "Estacionamiento publicado correctamente.")

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


@login_required
def pago(request, id):
    print("ID recibido en la vista pago:", id)
    estacionamiento_obj = get_object_or_404(Estacionamiento, id=id)

    # Obtener las tarjetas del usuario actual
    tarjetas_usuario = Tarjeta.objects.filter(user=request.user)

    context = {
        "TarjetaForm": TarjetaForm,
        "estacionamiento": estacionamiento_obj,
        "tarjetas_usuario": tarjetas_usuario,
    }
    return render(request, "pago.html", context)


def guardar_tarjeta(request):
    if request.method == "POST":
        num_tarjeta = request.POST.get("num_tarjeta")
        fecha_venc = request.POST.get("fecha_venc")
        cvv = request.POST.get("cvv")
        user_id = request.user.id

        print("Valor ingresado en 'num_tarjeta':", num_tarjeta)
        print("Valor ingresado en 'fecha_venc':", fecha_venc)
        print("Valor ingresado en 'cvv':", cvv)

        tarjeta = Tarjeta(
            num_tarjeta=num_tarjeta, fecha_venc=fecha_venc, cvv=cvv, user_id=user_id
        )
        tarjeta.save()
        messages.success(request, "Pago guardado correctamente.")

        return redirect("index")  # Redirige a la página de inicio

    return render(request, "index.html")


def generar_pago(request, id):
    if request.method == "POST":
        # Obtener datos del formulario
        hora_inic = request.POST.get("hora_inic")
        hora_fin = request.POST.get("hora_fin")
        patente = request.POST.get("patente")

        # Obtener el estacionamiento
        estacionamiento = Estacionamiento.objects.get(id=id)

        # Crear y guardar el arriendo
        arriendo = Arriendo(
            hora_inic=hora_inic,
            hora_fin=hora_fin,
            patente=patente,
            estacionamiento=estacionamiento,
        )
        arriendo.save()

        # Obtener los datos de la tarjeta seleccionada o nueva
        seleccion_tarjeta_id = request.POST.get("seleccion_tarjeta")
        if seleccion_tarjeta_id:
            # Utilizar una tarjeta existente
            tarjeta = Tarjeta.objects.get(id=seleccion_tarjeta_id)
        else:
            # Crear una nueva tarjeta
            num_tarjeta = request.POST.get("num_tarjeta")
            fecha_venc = request.POST.get("fecha_venc")
            cvv = request.POST.get("cvv")

            tarjeta = Tarjeta(
                num_tarjeta=num_tarjeta,
                fecha_venc=fecha_venc,
                cvv=cvv,
                user=request.user,
            )
            tarjeta.save()

        messages.success(request, "Arriendo pagado exitosamente.")
        return redirect("index")  # Redirige a la página de inicio

    return render(request, "pago.html")
