from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

# Página de inicio
def inicio(request):
    return render(request, 'tareas/index.html')

# Página ¿Quiénes Somos?
def quienes_somos(request):
    return render(request, 'tareas/quienes_somos.html')

# Página de Contacto y Envío de correos
def contactos(request):
    print("Método recibido:", request.method)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        asunto = f"Mensaje de {name}"
        cuerpo = f"Email: {email}\n\nMensaje:\n{message}"
        
        print(f"Nombre: {name}, Email: {email}, Mensaje: {message}")
        
        try:
            send_mail(
            asunto,
            cuerpo,
            settings.EMAIL_HOST_USER,  # De
            ['xolav9424@gmail.com'],   # Para
            fail_silently=False
        )   
            messages.success(request, '¡Tu mensaje ha sido enviado correctamente!')
        except Exception as e:
            messages.error(request, f'Error al enviar el mensaje: {e}')
        return redirect('contactos')  # Esto debe ser el nombre de la URL (no una plantilla)
    
    return render(request, 'tareas/contactos.html')

# Página de Productos: Aguas
def aguas(request):
    return render(request, 'tareas/productos/aguas.html')

# Página de Productos: Aguas_saborizadas
def aguas_saborizadas(request):
    return render(request, 'tareas/productos/aguas_saborizadas.html')

# Página de Productos: Jugos
def jugos(request):
    return render(request, 'tareas/productos/jugos.html')

# Página de Productos: Energizantes
def energizantes(request):
    return render(request, 'tareas/productos/energizantes.html')

# Página de Productos: Bebidas_isotonicas
def bebidas_isotonicas(request):
    return render(request, 'tareas/productos/bebidas_isotonicas.html')

# Página de Productos: Gseosas
def gaseosas(request):
    return render(request, 'tareas/productos/gaseosas.html')
