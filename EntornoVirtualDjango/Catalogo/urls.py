from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeCategory,name="Index"),
    path('productos/', views.ProductosListView.as_view(),name="product_list"),
    path('product_new/', views.ProductoCreateView.as_view(),name="product_new"),
    path('product_upd/<pk>', views.ProductoUpdateView.as_view(),name="product_upd"),
]
