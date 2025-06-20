# tareas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('contactos/', views.contactos, name='contactos'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('user_settings/', views.user_settings, name='user_settings'),
    path('eliminar_cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('aguas/', views.aguas, name='aguas'),
    path('productos/aguas-saborizadas/', views.aguas_saborizadas, name='aguas_saborizadas'),
    path('productos/jugos/', views.jugos, name='jugos'),
    path('productos/energizantes/', views.energizantes, name='energizantes'),
    path('productos/bebidas-isotonicas/', views.bebidas_isotonicas, name='bebidas_isotonicas'),
    path('productos/gaseosas/', views.gaseosas, name='gaseosas'),
]
