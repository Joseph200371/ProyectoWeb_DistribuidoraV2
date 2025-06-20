from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Import para Registro - Login - Logout
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroUsuarioForm

# Impor para user_settings - cerrar_sesion
from django.contrib.auth.decorators import login_required
from .forms import PerfilUsuarioForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

# Configuración del usuario
@login_required
def user_settings(request):
    user = request.user
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password1')
            if password:
                update_session_auth_hash(request, user)  # mantiene la sesión activa
            return redirect('user_settings')
    else:
        form = PerfilUsuarioForm(instance=user)
    return render(request, 'tareas/user_settings.html', {'form': form})


# Registro
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save() # aca estoy guardando en la BD
            messages.success(request, "Usuario creado correctamente")
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'tareas/registro.html', {'form': form})

# Inicio de sesion
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, "Credenciales incorrectas")
    return render(request, 'tareas/login.html')

# Cerrar sesion
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

# Eliminar cuenta
@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('index')

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
        return redirect('contactos')    
    return render(request, 'tareas/contactos.html')

# Página de Productos: Gseosas
def gaseosas(request):
    productos = [
        {
            "nombre": "Coca Cola 2.25lts x8un",
            "imagen": "tareas/img/product-cards/gaseosas/coca-cola-2.25lts.svg",
            "alt": "Pack Coca Cola 2.25lts"
        },
        {
            "nombre": "Coca Cola Cero 1.75lts x8un",
            "imagen": "tareas/img/product-cards/gaseosas/coca-cola-cero-1.75lts.svg",
            "alt": "Pack Coca Cola Cero 1.75lts"
        },
        {
            "nombre": "Coca Cola Lata 354cc x6un",
            "imagen": "tareas/img/product-cards/gaseosas/coca-cola-lata-354ml.svg",
            "alt": "Pack Coca Cola Lata 354ml"
        },
        {
            "nombre": "Pepsi 1.5lts x6un",
            "imagen": "tareas/img/product-cards/gaseosas/pepsi-1.5lts.jpg",
            "alt": "Pack Pepsi 1.5lts"
        },
        {
            "nombre": "Pepsi Black 1.5lts x6un",
            "imagen": "tareas/img/product-cards/gaseosas/pepsi-black-1.5lts.jpg",
            "alt": "Pack Pepsi Black 1.5lts"
        },
        {
            "nombre": "Pepsi Black Lata 354ml x6un",
            "imagen": "tareas/img/product-cards/gaseosas/pepsi-black-lata-354ml.jpg",
            "alt": "Pack Pepsi Black Lata 354ml"
        }
    ]
    return render(request, 'tareas/productos/gaseosas.html', {'productos': productos})

# Página de Productos: Aguas
def aguas(request):
    productos = [
        {
            "nombre": "Villavicencio con gas 1,5lts x6un",
            "imagen": "tareas/img/product-cards/aguas/villavicencio-con-gas-15lts.svg",
            "alt": "Pack Villavicencio con gas 1,5lts"
        },
        {
            "nombre": "Villavicencio con gas 500ml x12un",
            "imagen": "tareas/img/product-cards/aguas/villavicencio-con-gas-500cc.svg",
            "alt": "Pack Villavicencio con gas 500ml"
        },
        {
            "nombre": "Villavicencio 1,5lts x6un",
            "imagen": "tareas/img/product-cards/aguas/villavicencio-15lts.svg",
            "alt": "Pack Villavicencio 1,5lts"
        },
        {
            "nombre": "Villavicencio 500ml x12un",
            "imagen": "tareas/img/product-cards/aguas/villavicencio-500cc.svg",
            "alt": "Pack Villavicencio 500ml"
        },
        {
            "nombre": "Villamanaos 600ml x 12un",
            "imagen": "tareas/img/product-cards/aguas/villamanaos-600cc.svg",
            "alt": "Pack Villamanaos 600ml"
        },
        {
            "nombre": "Soda Manaos 2lts x6un",
            "imagen": "tareas/img/product-cards/aguas/soda-manaos-2lts.svg",
            "alt": "Soda Manaos 2lts"
        }
    ]
    return render(request, 'tareas/productos/aguas.html', {'productos': productos})

# Página de Productos: Aguas_saborizadas
def aguas_saborizadas(request):
    productos = [
        {
            "nombre": "Aquarius Manzana 1.5lts x6un",
            "imagen": "tareas/img/product-cards/aguas_saborizadas/aquarius-manzana-1.5lts.jpg",
            "alt": "Pack Aquarius Manzana 1.5lts"
        },
        {
            "nombre": "Aquarius Manzana 500ml x6un",
            "imagen": "tareas/img/product-cards/aguas_saborizadas/aquarius-manzana-500ml.svg",
            "alt": "Pack Aquarius Manzana 500ml"
        },
        {
            "nombre": "Aquarius Naranja 1.5lts x6un",
            "imagen": "tareas/img/product-cards/aguas_saborizadas/aquarius-naranja-1.5lts.jpg",
            "alt": "Pack Aquarius Naranja 1.5lts"
        },
        
        {
            "nombre": "Levite Naranja 1.5lts x6un",
            "imagen": "tareas/img/product-cards/aguas_saborizadas/levite-naranja-1.5lts.svg",
            "alt": "Pack Levite Naranja 1.5lts"
        },
        {
            "nombre": "Levite Pera 1.5lts x6un",
            "imagen": "tareas/img/product-cards/aguas_saborizadas/levite-pera-1.5lts.svg",
            "alt": "Pack Levite Pera 1.5lts"
        },
        {
            "nombre": "Levite Pomelo 1.5lts x6un",
            "imagen": "tareas/img/product-cards/aguas_saborizadas/levite-pomelo-1.5lts.svg",
            "alt": "Pack Levite Pomelo 1.5lts"
        },
    ]
    return render(request, 'tareas/productos/aguas_saborizadas.html', {'productos': productos})

# Página de Productos: Jugos
def jugos(request):
    productos = [
        {
            "nombre": "Baggio Manzana 1lts x8un",
            "imagen": "tareas/img/product-cards/jugos/baggio-manzana-1lts.jpg",
            "alt": "Pack Baggio Manzana 1lts"
        },
        {
            "nombre": "Baggio Naranja 1lts x8un",
            "imagen": "tareas/img/product-cards/jugos/baggio-naranja-1lts.jpg",
            "alt": "Pack Baggio Naranja 1lts"
        },
        {
            "nombre": "Baggio Manzana 200ml x18un",
            "imagen": "tareas/img/product-cards/jugos/baggio-manzana-200ml.jpg",
            "alt": "Pack Baggio Manzana 200ml"
        },
        {
            "nombre": "Baggio Naranja 200ml x18un",
            "imagen": "tareas/img/product-cards/jugos/baggio-naranja-200ml.jpg",
            "alt": "Pack Baggio Naranja 200ml"
        },
        {
            "nombre": "Cepita Naranja 1lts x6un",
            "imagen": "tareas/img/product-cards/jugos/cepita-naranja-botella-1lts.jpg",
            "alt": "Pack Cepita Naranja 1lts"
        },
        {
            "nombre": "Cepita Durazno 1lts x6un",
            "imagen": "tareas/img/product-cards/jugos/cepita-durazno-botella-1lts.jpg",
            "alt": "Pack Cepita Durazno 1lts"
        }
    ]
    return render(request, 'tareas/productos/jugos.html', {'productos': productos})

# Página de Productos: Energizantes
def energizantes(request):
    productos = [
        {
            "nombre": "Monster Blanco Sin azúcar 473ml x6un",
            "imagen": "tareas/img/product-cards/energizantes/monster-blanco-473ml.svg",
            "alt": "Pack Monster Blanco Sin Azúcar 473ml"
        },
        {
            "nombre": "Monster Negro 473ml x6un",
            "imagen": "tareas/img/product-cards/energizantes/monster-negro-473ml.svg",
            "alt": "Pack Monster Negro 473ml"
        },
        {
            "nombre": "Red Bull 250ml x24un",
            "imagen": "tareas/img/product-cards/energizantes/red-bull-250ml.jpeg",
            "alt": "Pack Red Bull 250ml"
        },
        {
            "nombre": "Red bull Sin Azúcar 250ml x24un",
            "imagen": "tareas/img/product-cards/energizantes/red-bull-sin-azucar-250ml.jpeg",
            "alt": "Pack Red Bull Sin Azúcar 250ml"
        },
        {
            "nombre": "Speed 250ml x24un",
            "imagen": "tareas/img/product-cards/energizantes/speed-250ml.svg",
            "alt": "Pack Speed 250ml"
        },
        {
            "nombre": "Speed 473ml x12un",
            "imagen": "tareas/img/product-cards/energizantes/speed-473ml.svg",
            "alt": "Pack Speed 473ml"
        }
    ]
    return render(request, 'tareas/productos/energizantes.html', {'productos': productos})

# Página de Productos: Bebidas_isotonicas
def bebidas_isotonicas(request):
    productos = [
        {
            "nombre": "Gatorade Blue 500ml x6un",
            "imagen": "tareas/img/product-cards/bebidas_isotonicas/gatorade-blue-500ml.svg",
            "alt": "Pack Gatorade Blue 500ml"
        },
        {
            "nombre": "Gatorade Manzana 500ml x6un",
            "imagen": "tareas/img/product-cards/bebidas_isotonicas/gatoradem-manzana-500ml.svg",
            "alt": "Pack Gatorade Manzana 500ml"
        },
        {
            "nombre": "Gatorade Rojo 500ml x6un",
            "imagen": "tareas/img/product-cards/bebidas_isotonicas/gatorade-rojo-500ml.svg",
            "alt": "Pack Gatorade Rojo 500ml"
        },
        {
            "nombre": "Powerade Blue 500ml x6un",
            "imagen": "tareas/img/product-cards/bebidas_isotonicas/powerade-blue-500ml.svg",
            "alt": "Pack Powerade Blue 500ml"
        },
        {
            "nombre": "Powerade Manzana 500ml x6un",
            "imagen": "tareas/img/product-cards/bebidas_isotonicas/powerade-manzana-500ml.svg",
            "alt": "Pack Powerade Manzana 500ml"
        },
        {
            "nombre": "Powerade Frutas tropicales Rojo 500ml x6un",
            "imagen": "tareas/img/product-cards/bebidas_isotonicas/powerade-rojo-500ml.svg",
            "alt": "Pack Powerade Frutas Tropicales 500ml"
        }
    ]
    return render(request, 'tareas/productos/bebidas_isotonicas.html', {'productos': productos})

# Esto hace que el navegador vea una URL distinta cada vez (y no use la caché).
# from django.utils.timezone import now

def mi_vista(request):
    return render(request, 'login.html', {'timestamp': now().timestamp()})

# views.py
def productos_bebidas(request):
    categorias = {
        "Aguas Saborizadas": [
            {"nombre": "Aquarius Manzana 1.5lts x6un", "imagen": "tareas/img/product-cards/aguas-saborizadas/aquarius-manzana-1.5lts.svg"},
            {"nombre": "Aquarius Manzana 500ml x6un", "imagen": "tareas/img/product-cards/aguas-saborizadas/aquarius-manzana-500ml.svg"},
            {"nombre": "Aquarius Naranja 1.5lts x6un", "imagen": "tareas/img/product-cards/aguas-saborizadas/aquarius-naranja-1.5lts.svg"},
            {"nombre": "Levite Naranja 1.5lts x6un", "imagen": "tareas/img/product-cards/aguas-saborizadas/levite-naranja-1.5lts.svg"},
            {"nombre": "Levite Pera 1.5lts x6un", "imagen": "tareas/img/product-cards/aguas-saborizadas/levite-pera-1.5lts.svg"},
            {"nombre": "Levite Pomelo 1.5lts x6un", "imagen": "tareas/img/product-cards/aguas-saborizadas/levite-pomelo-1.5lts.svg"},
        ],
        "Bebidas Isotónicas": [
            {"nombre": "Gatorade Blue 500ml x6un", "imagen": "tareas/img/product-cards/bebidas_isotonicas/gatorade-blue-500ml.svg"},
            {"nombre": "Gatorade Manzana 500ml x6un", "imagen": "tareas/img/product-cards/bebidas_isotonicas/gatoradem-manzana-500ml.svg"},
            {"nombre": "Gatorade Rojo 500ml x6un", "imagen": "tareas/img/product-cards/bebidas_isotonicas/gatorade-rojo-500ml.svg"},
            {"nombre": "Powerade Blue 500ml x6un", "imagen": "tareas/img/product-cards/bebidas_isotonicas/powerade-blue-500ml.svg"},
            {"nombre": "Powerade Manzana 500ml x6un", "imagen": "tareas/img/product-cards/bebidas_isotonicas/powerade-manzana-500ml.svg"},
            {"nombre": "Powerade Frutas tropicales Rojo 500ml x6un", "imagen": "tareas/img/product-cards/bebidas_isotonicas/powerade-rojo-500ml.svg"},
        ],
        "Energizantes": [
            {"nombre": "Monster Blanco Sin azúcar 473ml x6un", "imagen": "tareas/img/product-cards/energizantes/monster-blanco-473ml.svg"},
            {"nombre": "Monster Negro 473ml x6un", "imagen": "tareas/img/product-cards/energizantes/monster-negro-473ml.svg"},
            {"nombre": "Red Bull 250ml x24un", "imagen": "tareas/img/product-cards/energizantes/red-bull-250ml.jpeg"},
            {"nombre": "Red bull Sin Azúcar 250ml x24un", "imagen": "tareas/img/product-cards/energizantes/red-bull-sin-azucar-250ml.jpeg"},
            {"nombre": "Speed 250ml x24un", "imagen": "tareas/img/product-cards/energizantes/speed-250ml.svg"},
            {"nombre": "Speed 473ml x12un", "imagen": "tareas/img/product-cards/energizantes/speed-473ml.svg"},
        ],
        "Gaseosas": [
            {"nombre": "Coca Cola 2.25lts x8un", "imagen": "tareas/img/product-cards/gaseosas/coca-cola-2.25lts.svg"},
            {"nombre": "Coca Cola Cero 1.75lts x8un", "imagen": "tareas/img/product-cards/gaseosas/coca-cola-cero-1.75lts.svg"},
            {"nombre": "Coca Cola Lata 354cc x6un", "imagen": "tareas/img/product-cards/gaseosas/coca-cola-lata-354ml.svg"},
            {"nombre": "Pepsi 1.5lts x6un", "imagen": "tareas/img/product-cards/gaseosas/pepsi-1.5lts.jpg"},
            {"nombre": "Pepsi Black 1.5lts x6un", "imagen": "tareas/img/product-cards/gaseosas/pepsi-black-1.5lts.jpg"},
            {"nombre": "Pepsi Black Lata 354ml x6un", "imagen": "tareas/img/product-cards/gaseosas/pepsi-black-lata-354ml.jpg"},
        ],
        "Jugos": [
            {"nombre": "Baggio Manzana 1lts x8un", "imagen": "tareas/img/product-cards/jugos/baggio-manzana-1lts.jpg"},
            {"nombre": "Baggio Naranja 1lts x8un", "imagen": "tareas/img/product-cards/jugos/baggio-naranja-1lts.jpg"},
            {"nombre": "Baggio Manzana 200ml x18un", "imagen": "tareas/img/product-cards/jugos/baggio-manzana-200ml.jpg"},
            {"nombre": "Baggio Naranja 200ml x18un", "imagen": "tareas/img/product-cards/jugos/baggio-naranja-200ml.jpg"},
            {"nombre": "Cepita Naranja 1lts x6un", "imagen": "tareas/img/product-cards/jugos/cepita-naranja-botella-1lts.jpg"},
            {"nombre": "Cepita Durazno 1lts x6un", "imagen": "tareas/img/product-cards/jugos/cepita-durazno-botella-1lts.jpg"},
        ]
    }

    return render(request, 'tareas/productos/productos_bebidas.html', {'categorias': categorias})
