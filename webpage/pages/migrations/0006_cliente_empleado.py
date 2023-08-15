# Generated by Django 4.2.4 on 2023-08-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_tipocontrato_archivo_contrato_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(choices=[('PN', 'Persona Natural'), ('PJ', 'Persona Jurídica')], max_length=2)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('dni', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre_empresa', models.CharField(blank=True, max_length=255, null=True)),
                ('ruc', models.CharField(blank=True, max_length=11, null=True)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('posicion', models.CharField(max_length=255)),
                ('fecha_ingreso', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['id'],
            },
        ),
    ]