# Generated by Django 4.2.2 on 2023-12-12 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiEstacionamiento', '0007_remove_estacionamiento_run_remove_tarjeta_run_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arriendo',
            old_name='id_est',
            new_name='estacionamiento',
        ),
        migrations.RenameField(
            model_name='calificacion',
            old_name='id',
            new_name='arriendo',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='id_dir',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='ide',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tarjeta',
            old_name='ide',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='ide',
            new_name='user',
        ),
    ]