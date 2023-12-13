from django.shortcuts import render
from store.service import get_Categorias, get_Productos

# Create your views here.
def index(request):
    categorias = get_Categorias()
    productos = get_Productos()
    #for categoria in categorias:
    #   categoria['imagen'] = 'static/images/categorias'+ categoria['imagen'].split('/')[3]
    
    #data =  {
    #    'categorias':categorias
    #}
    print(categorias)
    print(productos)
    return render(request,'store/index2.html')