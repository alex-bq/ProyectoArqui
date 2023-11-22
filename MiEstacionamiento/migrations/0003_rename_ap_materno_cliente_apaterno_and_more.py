# Generated by Django 4.2.2 on 2023-11-22 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiEstacionamiento', '0002_marca_arriendo_estado_modelo_calificacion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='ap_materno',
            new_name='aPaterno',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='dv_run',
            new_name='dv',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='clave',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='run_cli',
            new_name='run',
        ),
        migrations.RenameField(
            model_name='dueno',
            old_name='ap_materno',
            new_name='aPaterno',
        ),
        migrations.RenameField(
            model_name='dueno',
            old_name='dv_run',
            new_name='dv',
        ),
        migrations.RenameField(
            model_name='dueno',
            old_name='clave',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='dueno',
            old_name='run_due',
            new_name='run',
        ),
        migrations.RenameField(
            model_name='tarjeta',
            old_name='run_cli',
            new_name='run',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='run_cli',
            new_name='run',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='ap_paterno',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='fec_nac',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='s_nombre',
        ),
        migrations.RemoveField(
            model_name='dueno',
            name='ap_paterno',
        ),
        migrations.RemoveField(
            model_name='dueno',
            name='fec_nac',
        ),
        migrations.RemoveField(
            model_name='dueno',
            name='s_nombre',
        ),
    ]
