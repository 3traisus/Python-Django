from rest_framework.generics import ListAPIView
from .models import Producto
from Productos.serializers import ProductoSerializers
# Create your views here.
class ProductoListApiView(ListAPIView):
    def get_queryset(self):
        #Realiza la consulta a la base de datos
        return Producto.objects.all()
    
    serializer_class = ProductoSerializers
    