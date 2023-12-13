from django.urls import path
from . import views 

urlpatterns = [
    path('api/producto/list/',views.ProductoListApiView.as_view(),name='Producto-list'),
]

