# Generated by Django 4.2.7 on 2023-12-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiEstacionamiento', '0013_tarjeta_fecha_venc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='user',
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='patente',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_venc',
            field=models.CharField(max_length=7),
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Modelo',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
