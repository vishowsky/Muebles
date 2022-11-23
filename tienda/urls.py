from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('categorias', views.categorias, name='categorias'),
    path('categorias/<str:slug>', views.categoriasview, name="categoriasview"),
    path('categorias/<str:categoriaSlug>/<str:productoSlug>', views.productosview, name="productosview"),
]

