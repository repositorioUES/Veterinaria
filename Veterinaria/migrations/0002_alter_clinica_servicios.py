# Generated by Django 3.2.4 on 2021-06-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinica',
            name='servicios',
            field=models.CharField(max_length=100),
        ),
    ]
