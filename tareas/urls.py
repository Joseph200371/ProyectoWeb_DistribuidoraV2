# tareas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('contactos/', views.contactos, name='contactos'),
    path('aguas/', views.aguas, name='aguas'),
    path('productos/aguas-saborizadas/', views.aguas_saborizadas, name='aguas_saborizadas'),
    path('productos/jugos/', views.jugos, name='jugos'),
    path('productos/energizantes/', views.energizantes, name='energizantes'),
    path('productos/bebidas-isotonicas/', views.bebidas_isotonicas, name='bebidas_isotonicas'),
    path('productos/gaseosas/', views.gaseosas, name='gaseosas'),
]
