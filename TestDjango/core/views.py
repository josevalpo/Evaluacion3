from turtle import home
from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def index2(request):
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

# def productos(request):
#     return render(request, 'core/productos.html')

def productos(request):
    datos = {}
    return render(request, 'core/productos.html', datos)

# def form_producto(request):
#     return render(request, 'core/form_producto.html')

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_producto.html', datos)

# def form_mod_producto(request):
#     return render(request, 'core/form_mod_producto.html')

def form_mod_producto(request, id):
    producto = Producto.objects.get(sku=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos modificados correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

# def form_del_producto(request):
#     return render(request, 'core/form_del_producto.html')

def form_del_producto(request, id):
    producto = Producto.objects.get(sku=id)
    producto.delete()
    return redirect(to="productos")