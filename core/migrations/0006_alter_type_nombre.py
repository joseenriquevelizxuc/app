# Generated by Django 3.2.7 on 2021-10-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211003_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='Nombre',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
