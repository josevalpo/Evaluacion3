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

