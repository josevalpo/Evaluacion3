from turtle import home
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def bandanas(request):
    return render(request, 'core/bandanas.html')

def correas(request):
    return render(request, 'core/correas.html')

def identificadores(request):
    return render(request, 'core/identificadores.html')

def bandana_producto_1(request):
    return render(request, 'core/bandana_producto_1.html')

def correa_producto_1(request):
    return render(request, 'core/correa_producto_1.html')

def identificador_producto_1(request):
    return render(request, 'core/identificador_producto_1.html')

def registro(request):
    return render(request, 'core/registro.html')

