
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include
from recepcionista.views import viewRecepcionista, asignarRepartidor, cambiarEstado, menuRecepcion, cambiarEstadoTienda,verReclamos,detalleReclamo,cancelarPedidoRecepcionista,cambiarAPreparacionRecepcion,cambiarAPendienteRecepcion,cambiarAListoRecepcion

from registroDeUsuarios.views import registroUsuario
from proveedorMenu.views import menuProveedor, subirPlatilloProveedor, listarPlatilloProveedor, EliminarPlatilloProveedor, ModificarPlatilloProveedor, PlatillosPendientes, cambiarAPreparacion, cambiarAPendiente, cambiarAListo
from Home.views import inicio
from RegisterPlatillo.views import registroPlatillo
from repartidor.views import viewPedido, viewRepartidor, PerfilRepartidor, MiVehiculo, cambiarEstadoTiendaRepartidor
from reclamo.views import reclamo
from Home.views import quienesSomos
from administracion.urls import url_patterns
from PerfilUsuario.views import PerfilUsuario, perfilMenu, CambiarContra, estadoPedido,crearReclamo,crearMenu, cancelarPedido
from Platillos.views import platillos, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, guardar, FinalizarCompra, agregar_producto_fin, restar_producto_fin,agregar_producto_menu, platilloRut
from detallePedido.views import detallePedido
from administracion.views import pag_404


urlpatterns = [

    path('', inicio, name="home"),
    path('admin/', admin.site.urls, name="administracion"),
    path('administracion/', include(url_patterns)),
    path('registroPlatillo', registroPlatillo),
    path('reclamo', reclamo),
    path('quienesSomos', quienesSomos, name='quienesSomos'),
    # despues id en la ruta para filtro
    path('Historial/<id>', PerfilUsuario, name="historial"),
    path('platillos', platillos, name="platillos"),
    path('platilloRut', platilloRut, name="platilloRut"),
    path('perfilMenu/<id>', perfilMenu, name="perfilMenu"),
    path('menuProveedor/<id>', menuProveedor, name="menuProveedor"),
    path('SubirMisPlatillos', subirPlatilloProveedor, name="SubirMisPlatillos"),
    path('listarPlatilloProveedor', listarPlatilloProveedor,name="listarPlatilloProveedor"),
    path('EliminarPlatilloProveedor/<id>', EliminarPlatilloProveedor, name="EliminarPlatilloProveedor"),
    path('ModificarPlatilloProveedor/<id>', ModificarPlatilloProveedor, name="ModificarPlatilloProveedor"),
    path('PlatillosPendientes', PlatillosPendientes, name="PlatillosPendientes"),
    path('cambiarAPreparacion/<id>', cambiarAPreparacion, name="cambiarAPreparacion"),
    path('cambiarAPendiente/<id>', cambiarAPendiente, name="cambiarAPendiente"),
    path('cambiarAListo/<id>', cambiarAListo, name="cambiarAListo"),
    path('viewPedido/<id>', viewPedido, name="viewPedido"),
    path('FinalizarRepartidor/<id>', cambiarEstadoTiendaRepartidor, name="FinalizarRepartidor"),
    path('estadoPedido/<id>', estadoPedido, name="estadoPedido"),
    path('crearReclamo/<id>', crearReclamo, name="crearReclamo"),
    path('verReclamos', verReclamos, name="verReclamos"),
    path('detalleReclamo/<id>', detalleReclamo, name="detalleReclamo"),
    path('cancelarPedidoRecepcionista/<id>', cancelarPedidoRecepcionista, name="cancelarPedidoRecepcionista"),
    
    path('cambiarAPreparacionRecepcion/<id>/<id2>', cambiarAPreparacionRecepcion, name="cambiarAPreparacionRecepcion"),
    path('cambiarAPendienteRecepcion/<id>/<id2>', cambiarAPendienteRecepcion, name="cambiarAPendienteRecepcion"),
    path('cambiarAListoRecepcion/<id>/<id2>', cambiarAListoRecepcion, name="cambiarAListoRecepcion"),


    
    path('repartidor', viewRepartidor, name="repartidor"),
    path('perfilRepartidor/<id>', PerfilRepartidor, name="perfilRepartidor"),
    path('detallePedido', detallePedido),
    path('detallePedido/<idpedido>/<id>', detallePedido),
    path('MiVehiculo/<id>', MiVehiculo, name='MiVehiculo'),
    path('registroUsuarios', registroUsuario, name='registro'),
    path('cambioContrasena', CambiarContra, name="cambioContrasena"),
    path('crearMenu/<id>', crearMenu, name="crearMenu"),

    
    path('cancelarPedido/<id>', cancelarPedido, name="cancelarPedido"),

    
    path('accounts/', include('django.contrib.auth.urls')),
    path('viewPedido/<id>', viewPedido),
    path('recepcionista', viewRecepcionista, name='recepcionista'),
    path('estado/<id>', cambiarEstado, name='estado'),
    path('asignacion/<id>', asignarRepartidor, name='asignacionRepartidor'),
    path('menuRecepcion/<id>', menuRecepcion, name='menuRecepcion'),
    path('cambiarEstadoTienda/<id>', cambiarEstadoTienda, name='cambiarEstadoTienda'),
    # carro
    path('agregar/<id>', agregar_producto, name="agregarProducto"),
    path('agregarmenu/<id>', agregar_producto_menu, name="agregarmenu"),

    path('agregarFin/<id>', agregar_producto_fin, name="agregar_producto_fin"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar_producto"),
    path('restarFin/<id>', restar_producto_fin, name="restar_producto_fin"),
    path('limpiarCarro', limpiar_carrito, name="limpiar_carrito"),
    path('guardar', guardar, name="guardar"),
    path('FinalizarCompra', FinalizarCompra, name="FinalizarCompra"),
    path('prueba/', pag_404),



    #Restablecer contraseña mediante correo electrónico
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name ="cambioContrasenaEmail.html"), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name ="restablecerEnviado.html"), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name ="restablecerContrasena.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view( template_name ="confirmaRestablecer.html"), name='password_reset_complete'),

]
# handler404 = 'administracion.views.pag_404'
