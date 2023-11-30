# Generated by Django 4.2.7 on 2023-11-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_surname', models.CharField(max_length=50)),
                ('customer_dni', models.CharField(db_column='customer_DNI', max_length=50)),
                ('dob', models.CharField(blank=True, max_length=50, null=True)),
                ('branch_id', models.DateField()),
                ('tipo_cliente', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
