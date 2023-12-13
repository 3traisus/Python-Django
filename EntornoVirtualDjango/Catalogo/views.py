from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from Catalogo.models import Categoria,Producto
from .forms import Producto

from .data import productos
from django.views.generic import ListView,CreateView,UpdateView

class ProductosListView(ListView):
    template_name ="Catalogos/Productos/producto_list.html"
    model = Producto
    context_object_name = 'productos'
    #4.paginacion
    paginate_by = 5
    
class ProductoCreateView(CreateView):
    #Especificar template que responde a la vista
    template_name = "Catalogos/Productos/producto_new.html"
    #Especificar la forma 
    form_class = Producto
    #Redireccionar 
    success_url = reverse_lazy ('categoria:product_list')
    
    def form_valid(self, form):
        #calculuar el precio normal 
        producto = form.save(commit=False)
        ganancia = producto.costo * producto.descuento
        producto.save()
        return super(Producto,self).form_valid(form)
    
class ProductoUpdateView(UpdateView):
    template_name = "Catalogos/Productos/producto_upd.html"
    #form_class = Producto
    #Campos que se desean modificar
    fields = ['nombre','ganancia'] 
    model = Producto
    success_url = reverse_lazy('categoria:product_list')
     
        
# Create your views here.
def homeCategory(request):
    categoria = list(Categoria.objects.values())
    categ = Categoria.objects.all()
    data = {
        'Categoria': categoria,
        'Categ':categ
    }
    return render(request,"Catalogos/Categorias/category_list.html",data)

def agregar_categoria(request):
    data = {
        'form' : CategoriaForm
    }
    #Verificar si el usuario ya presiono el boton de envio POST
    if request.method == "POST":
        #Crear Formulario con los datos enviados
        formulario = CategoriaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "Categoria Agregada"
        else:
            data["form"] = formulario #Regresar el formulario con los errores

    return render(request, 'catalogos/categorias/category_new.html', context=data)

