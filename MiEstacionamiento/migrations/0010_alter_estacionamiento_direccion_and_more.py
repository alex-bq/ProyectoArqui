# Generated by Django 4.2.2 on 2023-12-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiEstacionamiento', '0009_rename_tarifa_estacionamiento_valorminu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='estacionamiento',
            table=None,
        ),
    ]
