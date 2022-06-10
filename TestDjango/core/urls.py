from django.urls import path
from .views import index, bandanas, correas, identificadores

urlpatterns = [
    path('', index, name="index"),
]