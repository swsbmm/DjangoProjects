# Generated by Django 4.1.5 on 2023-01-20 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=15, unique=True, verbose_name='Dni')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_created', models.DateField(auto_now=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='hojaVida/%y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['-id'],
            },
        ),
    ]