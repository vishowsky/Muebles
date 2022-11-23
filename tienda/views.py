from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request, "tienda/index.html")

def categorias(request):
    categoria = Categoria.objects.filter(estado=0)
    context = {'categoria':categoria}
    return render(request, "tienda/categorias.html", context)

def categoriasview(request, slug):
    if(Categoria.objects.filter(slug=slug, estado=0)):
        productos = Producto.objects.filter(categoria__slug=slug)
        categoria= Categoria.objects.filter(slug=slug).first()
        context = {'productos': productos, 'categoria':categoria}
        return render(request, "tienda/productos/index.html", context)
    else:
        messages.warning(request, "categoria no encontrado")
        return redirect('categorias')

def productosview(request, categoriaSlug, productoSlug):
    if(Categoria.objects.filter(slug=categoriaSlug, estado=0)):
        if(Producto.objects.filter(slug=productoSlug, estado=0)):
            productos = Producto.objects.filter(slug=productoSlug, estado=0).first
            context = {'productos':productos}
        else:
            messages.warning(request, "producto no encontrado")
            return redirect('categorias')
    else:
        messages.error(request, "Categoria no encontrada")
        return redirect('categorias')
    return render(request, "tienda/productos/view.html", context)