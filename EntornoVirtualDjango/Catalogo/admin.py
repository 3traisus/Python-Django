from django.contrib import admin
from . import models

# Register your models here.
#admin.site.register(models.Categoria)
#admin.site.register(models.Producto)

#Para que funcione el slug 
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}
    
@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}