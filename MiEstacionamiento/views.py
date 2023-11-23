from django.shortcuts import render
from .models import *
from django import forms
from .forms import ClienteForm
from django.contrib import messages
from datetime import datetime
from .models import Vehiculo
from django.shortcuts import redirect

# Create your views here.

def index(request):
    lista_arriendos = Arriendo.objects.all()
    context = {
       'lista_arriendos': lista_arriendos}
    return render(request,"index.html", context)

def registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado exitosamente.')
    else:
        form = ClienteForm()
    return render(request, 'registro.html', {'form': form})


def guardar_arriendo(request):
    if request.method == 'POST':
        hora_inic = request.POST.get('hora_inic')
        hora_fin = request.POST.get('hora_fin')
        patente = request.POST.get('patente')
        estatus = request.POST.get('estatus')

        # Realiza las operaciones necesarias con los datos recibidos
        # Por ejemplo, guardar los datos en la base de datos
        arriendo = arriendoWardado(hora_inic=hora_inic, hora_fin=hora_fin, patente=patente, estatus=estatus)
        arriendo.save()
        messages.success(request, 'Arriendo guardado exitosamente.')

        return redirect('index')  # Redirecciona a la página de inicio

    return render(request, 'index.html')







