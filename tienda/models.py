from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def rutaArchivo(request, nombreArchivo):
    nombreOriginal = nombreArchivo
    nowtime = datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    nombreArchivo = "%s%s" % (nowtime, nombreOriginal)
    return os.path.join('uploads/', nombreArchivo)
#
class Categoria(models.Model): 
    slug = models.CharField(max_length=150, null=False, blank=False )
    nombreCategoria = models.CharField(max_length=150, null=False, blank=False)
    imagenCategoria = models.ImageField(upload_to=rutaArchivo, null=True, blank=True)
    estado = models.BooleanField(default=False, help_text="0=habilitado, 1=desabilitado" )

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=150, null=False, blank=False)
    imagenProducto = models.ImageField(upload_to=rutaArchivo, null=True, blank=True)
    descripcionProducto = models.TextField(max_length=500, null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    estado = models.BooleanField(default=False, help_text="0=Disponible, 1=Sin stock" )
    etiqueta = models.CharField(max_length=150, null=False, blank=False)
    Trending = models.BooleanField(default=False, help_text="0=sin tendencia, 1=en tendencia" )
    diaDeCreacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombreProducto