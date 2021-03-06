# Generated by Django 3.2.4 on 2021-10-02 18:29

import Veterinaria.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0017_auto_20210913_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora',
            field=models.CharField(help_text=' Formato de Hora: ##:##', max_length=5, validators=[Veterinaria.validators.formato_Hora]),
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAplic', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=100)),
                ('lote', models.CharField(max_length=10)),
                ('fechaProx', models.DateField(validators=[Veterinaria.validators.fecha_mayor])),
                ('aplicador', models.CharField(max_length=70, validators=[Veterinaria.validators.solo_Letras])),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.paciente')),
            ],
        ),
    ]
