"""ElComilon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from RegisterRepartidor.views import Registrorep
from recepcionista.views import viewRecepcionista,asignarRepartidor, cambiarEstado
from registroDeUsuarios.views import registroUsuario
# from ElComilon.listarPlatillos.views import modificarPlatillo
from Home.views import inicio
from RegisterPlatillo.views import registroPlatillo
from Register.views import register, perfil
from registroProveedor.views import registroProveedor

from repartidor.views import viewPedido, viewRepartidor
from reclamo.views import reclamo
from Home.views import quienesSomos
from administracion.urls import url_patterns
from PerfilUsuario.views import PerfilUsuario
from Pedido.views import pedido
from Platillos.views import platillos, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

from detallePedido.views import detallePedido
from Menu.views import menu, crearMenu
from repartidor.views import viewRepartidor, viewPedido


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="home"),
    path('registroPlatillo', registroPlatillo),
    path('registro', register),
    path('registroProveedor', registroProveedor),
    path('reclamo', reclamo),
    path('quienesSomos', quienesSomos),
    path('Historial/<id>', PerfilUsuario, name="historial"),  # despues id en la ruta para filtro
    path('pedido', pedido),
    path('platillos', platillos, name="platillos"),
    path('regin', Registrorep, name="regin"),
    path('repartidor', viewRepartidor),
    path('viewPedido/<id>', viewPedido),
    path('detallePedido', detallePedido),
    path('detallePedido/<idpedido>/<id>', detallePedido),
    path('registroUsuarios', registroUsuario),
    path('administracion/', include(url_patterns)),


    path('menu/<id>', menu, name="menu"),
    path('crearMenu/<id>', crearMenu, name="crearMenu"),


    path('accounts/', include('django.contrib.auth.urls')),
    path('repartidor', viewRepartidor),
    path('viewPedido/<id>', viewPedido),     
    path('recepcionista', viewRecepcionista, name='recepcionista'),
    path('estado/<id>', cambiarEstado, name='estado'),
    path('asignacion/<id>', asignarRepartidor, name='asignacionRepartidor'),
    # carro
    path('agregar/<id>', agregar_producto, name="agregarProducto"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar_producto"),
    path('limpiarCarro', limpiar_carrito, name="limpiar_carrito"),

]
