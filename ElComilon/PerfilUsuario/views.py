from django.conf.urls import url
from django.contrib.auth.models import User
from core.models import Cliente, Pedido
from .forms import EditarCliente, EditarUsuario,EditarContrasena
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection
from django.core.paginator import Paginator
from django.http.response import Http404
from recepcionista.views import cambiar_estado
import base64
import cx_Oracle
# Create your views here.

def PerfilUsuario(request, id):
    # historial
    usuario = get_object_or_404(Cliente, idcuenta=id)
    page = request.GET.get('page',1)
    Lista = Pedido.objects.filter(rutcliente=usuario.rutcliente).order_by('-fechapedido')
    cliente = get_object_or_404(Cliente, idcuenta=id)
    try:
        paginator = Paginator(Lista, 9)
        Lista = paginator.page(page)
    except :
        raise Http404
    data = {
        'entity': Lista,
        'paginator' : paginator,
        'usuario': usuario,
        'cliente':cliente

    }
    return render(request, 'historialPedidos.html', data)


def perfilMenu(request, id):
    usuario = get_object_or_404(User, id=id)
    cliente = get_object_or_404(Cliente, idcuenta=id)
    
    formCuenta = EditarUsuario(instance=usuario)
    formPersonal = EditarCliente(instance=cliente)
    data = {
        'usuario': usuario,
        'formCuenta': formCuenta,
        'form': formPersonal,
        'cliente':cliente
    }
    if request.method == 'POST':
        formCuenta = EditarUsuario(request.POST, instance=request.user)
        formPersonal = EditarCliente(request.POST, instance=cliente)
    if formCuenta.is_valid():
        if formPersonal.is_valid():
            formCuenta.save()
            formPersonal.save()
            messages.success(request, "Modificado correctamente")
            usuario = get_object_or_404(User, id=id)
            cliente = get_object_or_404(Cliente, idcuenta=id)
            formCuenta = EditarUsuario(instance=usuario)
            formPersonal = EditarCliente(instance=cliente)
            data = {
                    'usuario': usuario,
                    'formCuenta': formCuenta,
                    'form': formPersonal
            }
            return render(request, 'perfilMenu.html', data)
    return render(request, 'perfilMenu.html', data)



@login_required()
def CambiarContra(request):
    data = {
        'form': EditarContrasena(user=request.user)
    }
    if request.method == 'POST':
        form = EditarContrasena(data=request.POST, user=request.user)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Contraseña Modificada Correctamente. Por favor, ingrese de nuevo")
            return redirect('login')
        data = {'form': form}
    return render(request, 'CambioContrasena.html', data)

def estadoPedido(request, id):
    cliente = get_object_or_404(Cliente, idcuenta = id)
    rut = cliente.rutcliente
    data= {
        'pedidos':listado_pedidos(rut),
        'cliente':cliente
    }
    return render(request, 'estadoPedido.html', data)

def cancelarPedido(request, id):
    cambiar_estado(id, 6)
    url='/estadoPedido/'+str(request.user.id)
    return redirect(to=url)

def listado_pedidos(rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PEDIDOS_PEND", [rut, out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def crearReclamo(request,id):
    cliente = get_object_or_404(Cliente, idcuenta=request.user.id)

    data={
        'id': id,
    }
    if request.method =='POST':
        descripcion =  request.POST.get('desc')
        registrarReclamo(descripcion,cliente.rutcliente)
        messages.success(request,'Reclamo enviado')
        return render(request,'crearReclamo.html',data)        
    return render(request,'crearReclamo.html',data)


def registrarReclamo(descripcion,rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salidaPrve = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_RECLAMO",[descripcion,rut, salidaPrve])
    return salidaPrve.getvalue()




def crearMenu(request,id):
    cliente =  get_object_or_404(Cliente,idcuenta = id)
    
    data = {
        'menu':listado_menu(cliente.rutcliente),
        'platillos':listado_platillos(),
        'cliente':cliente
    }
  
    if request.method == 'POST':
        dia = request.POST.get('dia')
        idplatillo = request.POST.get('platillo')
        rut = cliente.rutcliente

        eliminarMenu(dia,rut)
        registrarMenu(dia,idplatillo, rut)
        data = {
            'menu':listado_menu(cliente.rutcliente),
            'platillos':listado_platillos(),
            'cliente':cliente
        }
        return render(request, 'menu.html', data)
    return render(request, 'menu.html', data)


def listado_platillos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PLATILLOS", [out_cur])    

    lista = []
    for fila in out_cur:
        data = {
            'data':fila,
            'imagen':str(base64.b64encode(fila[4].read()), 'utf-8')
        }
        lista.append(data)

    return lista

def registrarMenu(dia,idplatillo, rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("SP_INSERT_MENU",[dia,idplatillo, rut])
    return 0

def eliminarMenu(dia, rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("SP_ELIMINAR_MENU",[dia, rut])
    return 0


def listado_menu(rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_MENU", [rut,out_cur])    

    lista = []
    for fila in out_cur:
        data = {
            'data':fila
        }
        lista.append(data)

    return lista