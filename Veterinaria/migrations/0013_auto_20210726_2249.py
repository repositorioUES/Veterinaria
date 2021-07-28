# Generated by Django 3.2.4 on 2021-07-27 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0012_auto_20210724_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='clinica',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.clinica'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='horario',
            name='clinica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.clinica'),
        ),
    ]
