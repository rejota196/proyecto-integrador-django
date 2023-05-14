from django.shortcuts import render,redirect
from .models import Producto,Proveedor

# Create your views here.
def cargar_home(request):
    return render(request, 'home.html')

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        proveedor_id = request.POST.get('proveedor')
        if not Proveedor.objects.exists(): 
            return redirect('/compras/proveedores/crear')
        proveedor = Proveedor.objects.get(id=proveedor_id)
        producto = Producto(nombre=nombre, precio=precio, stock_actual=stock_actual, proveedor=proveedor)
        producto.save()
        return redirect('/compras/productos/crear')
    else:
        proveedores = Proveedor.objects.all()
        return render(request, 'agregar_producto.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        proveedor = Proveedor(nombre=nombre, apellido=apellido, dni=dni)
        proveedor.save()
        return redirect('/compras/proveedores/crear')
    else:
        return render(request, 'agregar_proveedor.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})
