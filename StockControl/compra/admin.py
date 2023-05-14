from django.contrib import admin
from compra.models import Producto, Proveedor

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display =  ('id', 'nombre', 'apellido', 'dni')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock_actual', 'proveedor')    

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
