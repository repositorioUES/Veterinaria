# Generated by Django 3.2.4 on 2021-06-22 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='Ingrese un departamento', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='Ingrese un municipio', max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Veterinaria.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('dui', models.CharField(help_text='Número de DUI', max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fechaNacim', models.DateField(blank=True)),
                ('edad', models.IntegerField(help_text='Se calculará automaticamente')),
                ('direccion', models.CharField(help_text='Calle, Colonia, Cantón ...', max_length=100)),
                ('correo', models.CharField(help_text='Correo Electrónico', max_length=50)),
                ('telefono', models.CharField(help_text='Telefono de contacto', max_length=50)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Veterinaria.departamento')),
                ('municipio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Veterinaria.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to='images')),
                ('nombre', models.CharField(help_text='Nombre del paciente', max_length=50)),
                ('sexo', models.CharField(blank=True, choices=[('m', 'Macho'), ('h', 'Hembra')], help_text='Sexo del paciente', max_length=10)),
                ('especie', models.CharField(help_text='Especie del paciente', max_length=50)),
                ('raza', models.CharField(help_text='Raza del paciente', max_length=50)),
                ('color', models.CharField(help_text='Color del paciente', max_length=50)),
                ('fechaNacim', models.DateField(blank=True)),
                ('observaciones', models.CharField(help_text='Las que considere peertinentes', max_length=500)),
                ('activo', models.IntegerField(blank=True, default=1, max_length=1)),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Veterinaria.propietario')),
            ],
        ),
    ]
