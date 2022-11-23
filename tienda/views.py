from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, "tienda/index.html")

def categorias(request):
    categoria = Categoria.objects.filter(estado=0)
    context = {'categoria':categoria}
    return render(request, "tienda/categorias.html", context)

