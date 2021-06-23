# Generated by Django 3.2.4 on 2021-06-22 23:09

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
                ('dui', models.CharField(help_text='########-#', max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fechaNacim', models.DateField()),
                ('edad', models.IntegerField(help_text='Se calculará automaticamente')),
                ('direccion', models.CharField(help_text='Calle, Colonia, Cantón ...', max_length=100)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(help_text='####-####', max_length=9)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Veterinaria.departamento')),
                ('municipio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Veterinaria.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(null=True, upload_to='fotos')),
                ('nombrePac', models.CharField(max_length=50)),
                ('sexo', models.CharField(blank=True, choices=[('m', 'Macho'), ('h', 'Hembra')], max_length=10)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('fechaNacim', models.DateField(blank=True)),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('activo', models.IntegerField(blank=True, default=1, max_length=1)),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Veterinaria.propietario')),
            ],
        ),
    ]
