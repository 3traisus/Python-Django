from django.db import models
from django.utils.text import slugify


# Create your models here.


# Modelo de categoria
class Categoria(models.Model):
    clave = models.PositiveIntegerField(unique=True,blank=False,null=False)
    nombre = models.CharField(max_length=20,unique=True,blank=False,null=False)
    slug = models.SlugField(max_length=50)
    descripcion = models.TextField(blank=True,null=True,default="Descripcion...")
    descuento = models.DecimalField(max_digits=5,decimal_places=2)
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="categorias/",blank=True,null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False #permite que dijango haga cambios sobre la tabla
        db_table = 'Catalogo_categoria'


class Producto(models.Model):
    TIPO = (
        ("N","Nuevo"),
        ("M","Mas Vendido"),
        ("O","Ofertas"),
        ("L","Liquidacion"),
        ("I","Inventario")
    )
    PRESENTACION = (
        ("1","Botella"),
        ("2","Caja"),
        ("3","Paquete"),
        ("4","Regalo"),
    )
    id_prod = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=40)
    slug = models.CharField(unique=True, max_length=255)
    descrip = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=15)
    presentacion = models.CharField(max_length=15)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    ganancia = models.DecimalField(max_digits=4, decimal_places=2)
    descuento = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    existencia = models.IntegerField()
    imagen = models.CharField(max_length=100, blank=True, null=True)
    id_cat = models.ForeignKey(Categoria, models.DO_NOTHING)

    
    
    def __str__(self):
        return self.nombre
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.nombre)
        super(Producto, self).save(*args,**kwargs)
    
    class Meta:
        managed = False
        db_table = 'Catalogo_producto'
        #verbose_name_plural = "Catalago_producto"
