from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos_store'),
]
