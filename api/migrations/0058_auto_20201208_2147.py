# Generated by Django 3.1 on 2020-12-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_auto_20201208_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
