from django.shortcuts import render
from store.services import get_categorias, get_productos


# Create your views here.
def index(request):
    # Traer las categorias
    categorias = get_categorias()
    productos = get_productos()

    # Modificar la ruta de la imagen
    for producto in productos:
        producto['imagen'] = 'static/images/productos/' + producto['imagen'].split('/')[3]

    # Modificar la ruta de la imagen
    for categoria in categorias:
        categoria['imagen'] = 'static/images/categorias/' + categoria['imagen'].split('/')[3]

    data = {
        'categorias': categorias,
        'productos': productos,
    }

    return render(request, 'store/index.html', context=data)

def productos(request):
    # Traer las categorias
    categorias = get_categorias()
    productos = get_productos()

    # Modificar la ruta de la imagen
    for producto in productos:
        producto['imagen'] = '/static/images/productos/' + producto['imagen'].split('/')[3]

    # Modificar la ruta de la imagen
    for categoria in categorias:
        categoria['imagen'] = '/static/images/categorias/' + categoria['imagen'].split('/')[3]

    data = {
        'categorias': categorias,
        'productos': productos,
    }

    return render(request, 'store/product.html', context=data)