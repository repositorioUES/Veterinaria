# Generated by Django 3.2.4 on 2021-07-23 03:04

import Veterinaria.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0007_auto_20210722_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medico', models.CharField(max_length=70, validators=[Veterinaria.validators.solo_Letras])),
                ('edad', models.CharField(max_length=2, validators=[Veterinaria.validators.solo_Numeros])),
                ('peso', models.CharField(max_length=10)),
                ('fechaConsulta', models.DateField(auto_now_add=True)),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('medicamento', models.CharField(blank=True, max_length=200, null=True)),
                ('examenes', models.CharField(blank=True, max_length=200, null=True)),
                ('proximoCont', models.DateField(null=True, verbose_name='Fecha de Proximo Control')),
                ('hora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.horario', verbose_name='Hora de Cita')),
                ('pacienteId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.paciente')),
            ],
        ),
    ]
