# Generated by Django 3.1 on 2022-04-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0171_auto_20220419_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagotarjeta',
            name='proveedor',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pagotarjeta',
            name='servicio',
            field=models.CharField(default='', max_length=255),
        ),
    ]
