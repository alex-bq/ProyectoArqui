# Generated by Django 4.2.2 on 2023-11-23 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiEstacionamiento', '0004_rename_id_arr_arriendo_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='arriendoWardado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hora_inic', models.DateTimeField()),
                ('hora_fin', models.DateTimeField()),
                ('patente', models.CharField(max_length=6)),
                ('estatus', models.CharField(choices=[('pendiente', 'Pendiente'), ('cancelado', 'Cancelado'), ('culminado', 'Culminado')], default='pendiente', max_length=20)),
            ],
            options={
                'db_table': 'arriendoWardado',
            },
        ),
    ]
