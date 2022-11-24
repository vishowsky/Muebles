from django.shortcuts import redirect, render
from django.contrib import messages
from tienda.models import Producto, Carrito
from django.http.response import JsonResponse

def agregarAlCarro(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            productoId = int(request.POST.get('.idProducto'))
            productoCheck = Producto.objects.get(id==productoId)
            if(productoCheck):
                if(Carrito.objects.filter(user=request.user.id, idProducto=productoId)):
                    return JsonResponse({'status': "Producto agregado al carro"})
                else:
                    productoCantidad = int(request.POST.get('productoCantidad'))
                    if productoCheck.cantidad >= productoCantidad:
                        Carrito.objects.create(user=request.user, idProducto=productoId, cantidadProducto=productoCantidad)
                        return JsonResponse({'status': "no se encontro el producto"})
                    else:
                        JsonResponse({'status': "No hay tantas existencias de este producto"})

            else:
                return JsonResponse({'status': "no se encontro el producto"})
        else:
            return JsonResponse({'status': "inciar sesion para continuar"})
        
    return redirect('/')