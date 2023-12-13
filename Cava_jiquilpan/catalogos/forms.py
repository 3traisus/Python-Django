
from django import forms

from catalogos.models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Categoria
        # fields = ['clave', 'nombre', 'descripcion', 'descuento', 'estado']
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['slug']
        fields = '__all__'
        labels = {
            'id_prod': 'ID del producto',
            'id_cat': 'Categoria',
            'nombre': 'Nombre corto',
            'slug': 'Liga al producto',
            'descr': 'Descripción',
            'tipo': 'Tipo del producto',
            'presentacion': 'Presentación',
            'costo': 'Costo',
            'ganancia': 'Ganancia',
            'descuento': 'Descuento',
            'existencia': 'Existencia inicial del producto',
            'imagen': 'Imagen representativa del producto'
        }
