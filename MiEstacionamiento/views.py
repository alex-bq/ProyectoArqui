from django.shortcuts import render
from .models import *
from django import forms
from .forms import ClienteForm
from django.contrib import messages

# Create your views here.

def index(request):
    lista_clientes = Cliente.objects.all()
    context = {
       'lista_clientes': lista_clientes
    }
    return render(request,"index.html", context)

def registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado exitosamente.')
    else:
        form = ClienteForm()
    return render(request, 'registro.html', {'form': form})







