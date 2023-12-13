from . import views
from django.urls import path

urlpatterns = [
    path('categorias/', views.listar_categoria, name='categoria_list'),
    path('categorias-new/', views.agregar_categoria, name='categoria_new'),
    path('categorias-update/<id>/', views.actualizar_categoria, name='categoria_update'),
    path('categorias-delete/<id>/', views.eliminar_categoria, name='categoria_delete'),

    # Rutas de productos
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos-new/', views.ProductoCreateView.as_view(), name='producto_new'),
    path('productos-update/<pk>', views.ProductoUpdateView.as_view(), name='producto_update'),
    #path('productos-delete/<pk>', views.ProductoDeleteView.as_view(), name='producto_delete'),
]
