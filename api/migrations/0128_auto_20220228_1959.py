# Generated by Django 3.1 on 2022-03-01 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0127_publicidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='cupones'),
        ),
    ]
