# Generated by Django 3.1 on 2021-12-15 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0115_datos_cupones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insignia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, unique=True)),
                ('imagen', models.ImageField(blank=True, upload_to='insignias')),
                ('servicio', models.CharField(max_length=25)),
                ('estado', models.BooleanField(default=True)),
                ('pedidos', models.PositiveIntegerField(default=0)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
