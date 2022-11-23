from django.urls import path
from . import views

from tienda.controller import authview


urlpatterns = [
    path('', views.home, name="home"),
    path('categorias', views.categorias, name='categorias'),
    path('categorias/<str:slug>', views.categoriasview, name="categoriasview"),
    path('categorias/<str:categoriaSlug>/<str:productoSlug>', views.productosview, name="productosview"),
    
    path('registro/', authview.registro, name="registro"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),
]

