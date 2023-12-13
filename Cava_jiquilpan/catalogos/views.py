from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalogos.models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm
from django.contrib import messages

from . import data as datalist


# Vistas basadas en clases
class ProductoListView(ListView):
    #datalist.InsertarProductos()
    # print("Iniciar la carga de productos:")
    # for producto in mis_productos:
    #     print("Grabando: ", producto)
    #     Producto.objects.create(
    #         id_producto=producto[0],
    #         id_categoria=get_object_or_404(Categoria, clave=producto[1]),
    #         nombre_corto=producto[2],
    #         slug=producto[3],
    #         nombre_largo=producto[4],
    #         descripcion=producto[5],
    #         tipo=producto[6],
    #         presentacion=producto[7],
    #         costo=producto[8],
    #         ganancia=producto[9],
    #         descuento=producto[10],
    #         existencia=producto[11],
    #         imagen=producto[12]
    #     )
    # print("Carga terminada!")

    # 1. Nombre del template a utilizar
    template_name = 'catalogos/productos/producto_list.html'

    # 2. Nombre del modelo
    model = Producto

    # 3. Nombre del contexto
    context_object_name = 'productos'

    # 4. Paginacion
    paginate_by = 10


class ProductoCreateView(CreateView):
    # 1. Especificar el template que responde a la vista
    template_name = 'catalogos/productos/producto_new.html'
    # 2. Especificar la forma
    form_class = ProductoForm
    # 3. Redireccionar
    success_url = reverse_lazy('catalogos:producto_list')

    # Este metodo se ejecuta una vez los datos son validados
    def form_valid(self, form):
        # Calcular el precio normal y de oferta
        producto = form.save(commit=False)
        ganancia = producto.costo * producto.ganancia / 100
        descuento = producto.costo * producto.descuento / 100
        producto.precio_normal = producto.costo + ganancia
        producto.precio_oferta = producto.precio_normal - descuento
        producto.save()
        return super(ProductoCreateView, self).form_valid(form)


class ProductoUpdateView(UpdateView):
    template_name = 'catalogos/productos/producto_update.html'
    # form_class = ProductoForm
    fields = ['nombre', 'ganancia', 'descuento', 'existencia']
    model = Producto
    success_url = reverse_lazy('catalogos:producto_list')


#class ProductoDeleteView(DeleteView):
#    template_name = 'catalogos/productos/producto_update.html'
#    model = Producto
#    success_url = reverse_lazy('catalogos:producto_list')


# Create your views here.
def listar_categoria(request):
    #datalist.InsertarCategorias()
    # Consulta a la BD: SELECT * FROM categorias
    categorias = Categoria.objects.all()
    data = {
        'categorias': categorias
    }
    return render(request, 'catalogos/categorias/categoria_list.html', data)


def agregar_categoria(request):
    data = {
        'form': CategoriaForm()
    }
    # Verificar si el usuario ya presiono el boton de envio, valida la informacion por metodo POST
    if request.method == 'POST':
        # Formulario con los datos enviados
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoria agregada!')
            return redirect(to='catalogos:categoria_list')
        else:
            data['form'] = formulario # Esto lo que hace es regresar el formulario con los errores
    return render(request, 'catalogos/categorias/categoria_new.html', data)


def actualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    data = {
        'form': CategoriaForm(instance=categoria)
    }
    # Si el usuario dijo ya dijo que si, POST
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoria actualizada!')
            return redirect(to='catalogos:categoria_list')
        # Si no es valido el formulario
        data['form'] = formulario

    return render(request, 'catalogos/categorias/categoria_update.html', data)


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, 'Categoria eliminada!')
    return redirect(to='catalogos:categoria_list')


