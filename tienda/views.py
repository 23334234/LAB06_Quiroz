from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria  

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()  
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto': producto})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()  
    return render(request, 'productos_por_categoria.html', {'productos': productos, 'categoria': categoria, 'categorias': categorias})



















