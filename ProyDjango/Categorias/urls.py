from django.urls import path
from . import views 

urlpatterns = [
    path('api/categoria/list/',views.CategoriaListApiView.as_view(),name='Categorias-list'),
    path('api/categoria/create/',views.CategoriaCreateApiView.as_view(),name='Categorias-craete'),
    path('api/categoria/retrieve/<pk>/',views.CategoriaRetrieveApiView.as_view(),name='Categorias-retrieve'),
]

