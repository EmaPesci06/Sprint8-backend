# Generated by Django 4.2.7 on 2023-11-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sucursales', '0001_initial'),
        ('Clientes', '0001_initial'),
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Sucursales.sucursal')),
                ('address_0', models.TextField(db_column='address')),
                ('country', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.empleado')),
            ],
        ),
    ]
