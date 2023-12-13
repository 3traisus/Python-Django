from django.db import models
from Categorias.models import Categoria
from django.utils.text import slugify

# Create your models here.
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
    id_prod = models.PositiveBigIntegerField(primary_key=True,blank=False)
    id_cat = models.ForeignKey(Categoria,on_delete=models.PROTECT) # model.CASCADE
    nombre =  models.CharField(max_length=40,unique=True,blank=False,null=False)
    slug = models.SlugField(max_length=255,unique=True)
    descrip = models.TextField(blank=True,null=True)
    tipo = models.CharField(max_length=15,choices=TIPO,default="Nuevo")
    presentacion = models.CharField(max_length=15,choices=PRESENTACION,default="Botella")
    costo = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    ganancia = models.DecimalField(max_digits=4,decimal_places=2,blank=False,null=False,default=20.0)
    descuento = models.DecimalField(max_digits=4,decimal_places=2,blank=True,null=True,default=0.0)
    existencia = models.IntegerField(blank=False,null=False)
    imagen =  models.ImageField(upload_to="productos/",blank=True,null=True)#install Pillow
    
    def __str__(self):
        return self.nombre
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.nombre)
        super(Producto, self).save(*args,**kwargs)
    
    class Meta:
        managed = False
        db_table = 'Catalogo_producto'
        #verbose_name_plural = "Catalago_producto"
