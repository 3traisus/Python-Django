from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView
from .models import Categoria
from Categorias.serializers import CateegoriaSerializers,CateegoriaClienteSerializers
# Create your views here.
class CategoriaListApiView(ListAPIView):
    def get_queryset(self):
        #Realiza la consulta a la base de datos
        return Categoria.objects.all()
    
    serializer_class = CateegoriaClienteSerializers
    
class CategoriaCreateApiView(CreateAPIView):
    serializer_class = CateegoriaSerializers

class CategoriaRetrieveApiView(RetrieveAPIView):
    serializer_class = CateegoriaSerializers
    queryset = Categoria.objects.all()