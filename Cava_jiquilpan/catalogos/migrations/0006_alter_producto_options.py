# Generated by Django 4.2.7 on 2023-12-01 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0005_alter_producto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'managed': False, 'verbose_name_plural': 'Catalago_producto'},
        ),
    ]