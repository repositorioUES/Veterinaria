# Generated by Django 3.2.5 on 2021-07-25 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0009_consultorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='clinica',
        ),
        migrations.AddField(
            model_name='empleado',
            name='consultorio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Veterinaria.consultorio'),
            preserve_default=False,
        ),
    ]
