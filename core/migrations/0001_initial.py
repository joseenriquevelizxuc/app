# Generated by Django 3.2.7 on 2021-10-04 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=150, verbose_name='Nombres')),
                ('DPI', models.CharField(max_length=13, unique=True, verbose_name='Dpi')),
                ('FechaRegistro', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Registro')),
                ('FechaCreado', models.DateField(auto_now=True)),
                ('FechaActualizacion', models.DateField(auto_now_add=True)),
                ('Edad', models.PositiveIntegerField(default=0)),
                ('Salario', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('Estado', models.BooleanField(default=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='Avatar/%Y/%m/%d')),
                ('Cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
                'ordering': ['id'],
            },
        ),
    ]
