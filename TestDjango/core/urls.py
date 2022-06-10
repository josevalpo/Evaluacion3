from django.urls import path
from .views import index, bandanas, correas, identificadores, bandana_producto_1, correa_producto_1, identificador_producto_1, registro

urlpatterns = [
    path('', index, name="index"),
    path('bandanas.html', bandanas, name="bandanas"),
    path('correas.html', correas, name="correas"),
    path('identificadores.html', identificadores, name="identificadores"),
    path('bandana_producto_1.html', bandana_producto_1, name="bandana_producto_1"),
    path('correa_producto_1.html', correa_producto_1, name="correa_producto_1"),
    path('identificador_producto_1.html', identificador_producto_1, name="identificador_producto_1"),
    path('registro.html', registro, name="registro"),
]