# Generated by Django 4.2.7 on 2023-12-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiEstacionamiento', '0012_remove_arriendowardado_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='fecha_venc',
            field=models.CharField(default=1.0, max_length=6),
            preserve_default=False,
        ),
    ]