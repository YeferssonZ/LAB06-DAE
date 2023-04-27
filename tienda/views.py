from django.shortcuts import get_object_or_404, render
from . models import Producto 

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:9]
    context = {'product_list': product_list}
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    return render(request, 'producto.html', {'producto': producto})

def gaseosas(request):
    productos = Producto.objects.filter(categoria__nombre='Gaseosas')
    return render(request, 'gaseosas.html', {'productos': productos})

def chocolates(request):
    productos = Producto.objects.filter(categoria__nombre='Chocolates')
    return render(request, 'chocolates.html', {'productos': productos})

def galletas(request):
    productos = Producto.objects.filter(categoria__nombre='Galletas')
    return render(request, 'galletas.html', {'productos': productos})

def snacks(request):
    productos = Producto.objects.filter(categoria__nombre='Snacks')
    return render(request, 'snacks.html', {'productos': productos})