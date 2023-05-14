from django.urls import path
from compra import views

urlpatterns = [
    path('', views.cargar_home),
    path('compras/productos/crear', views.agregar_producto, name= 'agregar_producto'),
    path('compras/proveedores/crear', views.agregar_proveedor, name='agregar_proveedor'),
    path('compras/productos/listado', views.lista_productos, name= 'lista_productos'),
    path('compra/proveedores/listado', views.lista_proveedores, name= 'lista_proveedores'),
]
