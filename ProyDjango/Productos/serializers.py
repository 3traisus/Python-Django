from rest_framework import serializers
from .models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')
        #fields = ('id_prod','id_cat','nombre','tipo','costo','ganancia','descuento','imagen') 