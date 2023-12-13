from .models import Categoria, Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['slug']
        fields = '__all__'
        labels = {
            'id_prod' : 'ID',
            'id_cat' : 'Categoria',
            'nombre' :  'Nombre',
            'descrip' :'Descripcion',
            'tipo' : 'Tipo',
            'presentacion' : 'Presentacion',
            'costo' : 'Costo',
            'ganancia' : 'Ganancia',
            'descuento' : 'Descuento',
            'existencia' : 'Existencia',
            'imagen' :  'Imagen',
        }