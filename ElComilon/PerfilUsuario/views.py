from django.shortcuts import get_object_or_404, render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import EditarUsuario, EditarCliente
from core.models import Cliente, Pedido

# Create your views here.


def PerfilUsuario(request, id):
    # historial
    usuario = get_object_or_404(Cliente, idcuenta=id)
    pedido = Pedido.objects.filter(
        rutcliente=usuario.rutcliente).order_by('-fechapedido')
    data = {
        'usuario': usuario,
        'pedidos': pedido,
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
        'form': formPersonal
    }
    if request.method == 'POST':
        formCuenta = EditarUsuario(request.POST, instance=request.user)
        formPersonal = EditarCliente(request.POST, instance=cliente)
        if formCuenta.is_valid():
            if formPersonal.is_valid():
                formCuenta.save()
                formPersonal.save()
                usuario = get_object_or_404(User, id=id)
                cliente = get_object_or_404(Cliente, idcuenta=id)
                formCuenta = EditarUsuario(instance=usuario)
                formPersonal = EditarCliente(instance=cliente)
                data2 = {
                    'usuario': usuario,
                    'formCuenta': formCuenta,
                    'form': formPersonal
                }
                return render(request, 'perfilMenu.html', data2)
    return render(request, 'perfilMenu.html', data)


@login_required()
def CambiarContra(request):
    form = PasswordChangeForm(user=request.user)
    forumulario = {'form': form}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'CambioContrasena.html', forumulario)
