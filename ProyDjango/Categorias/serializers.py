from rest_framework import serializers
from .models import Categoria

class CateegoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        #fields = ('__all__')
        fields = ('clave','nombre','descripcion','descuento','estado','imagen')
        
class CateegoriaClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        #fields = ('__all__')#Muestra todos los campos 
        fields = ('nombre','descripcion','descuento','estado','imagen')