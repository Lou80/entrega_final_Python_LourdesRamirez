# Generated by Django 5.1.4 on 2024-12-29 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_alter_consumo_fecha_consumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.usuario', verbose_name='paciente'),
        ),
    ]
