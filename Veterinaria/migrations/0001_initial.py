# Generated by Django 3.2.4 on 2021-06-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dueño', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.TextField()),
                ('horarios', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=9)),
                ('servicios', models.CharField(max_length=20)),
            ],
        ),
    ]
