from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    lista_clientes = Cliente.objects.all()
    context = {
       'lista_clientes': lista_clientes
    }
    return render(request,"index.html", context)

def registro(request):
    return render(request,"registro.html")







