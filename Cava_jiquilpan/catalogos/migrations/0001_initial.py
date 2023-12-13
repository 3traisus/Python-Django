# Generated by Django 4.2.7 on 2023-12-01 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.PositiveIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField()),
                ('descripcion', models.TextField(blank=True, default='Descripcion', null=True)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estado', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='categorias/')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_corto', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('nombre_largo', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('N', 'Nuevo'), ('M', 'Mas vendido'), ('O', 'Ofertas'), ('L', 'Liquidacion'), ('I', 'Inventario')], default='Nuevo', max_length=15)),
                ('presentacion', models.CharField(choices=[('3', 'Paquete'), ('2', 'Caja'), ('1', 'Botella'), ('4', 'Regalo')], default='Botella', max_length=15)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('ganancia', models.DecimalField(decimal_places=2, default=20.0, max_digits=4)),
                ('descuento', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True)),
                ('precio_normal', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('precio_oferta', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('existencia', models.PositiveIntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.categoria')),
            ],
            options={
                'verbose_name_plural': 'Prodcutos',
            },
        ),
    ]
