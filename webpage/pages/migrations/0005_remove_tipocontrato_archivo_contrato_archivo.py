# Generated by Django 4.2.4 on 2023-08-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_tipocontrato_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipocontrato',
            name='archivo',
        ),
        migrations.AddField(
            model_name='contrato',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='upload/documento', verbose_name='URL Document'),
        ),
    ]
