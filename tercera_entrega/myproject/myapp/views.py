from django.shortcuts import render, redirect
from .models import Categoria, Producto, Orden
from .forms import CategoriaForm, ProductoForm, OrdenForm, BusquedaForm



def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save()  # Guarda el nuevo producto
            # Puedes realizar acciones adicionales aquí si es necesario
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def mi_vista(request):
    form = BusquedaForm()

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            # Procesar la búsqueda
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'form': form})

    return render(request, 'mi_template.html', {'form': form})