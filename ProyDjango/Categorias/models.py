from django.db import models

# Create your models here.
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
    
    #def save(self, *args,**kwargs):
    #    self.nombre = self.nombre.upper()
    #    self.descripcion = self.descripcion.upper()
    #    self.slug = slugify(self.nombre)
    #    super(Categoria, self).save(*args,**kwargs)
        