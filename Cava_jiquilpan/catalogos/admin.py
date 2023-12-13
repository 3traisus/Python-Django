from django.contrib import admin

import catalogos.models

# Register your models here.
# admin.site.register(catalogos.models.Categoria)
# admin.site.register(catalogos.models.Producto)

@admin.register(catalogos.models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(catalogos.models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
