# Generated by Django 3.1 on 2021-12-19 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0117_insignia_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos',
            name='cupones',
        ),
        migrations.CreateModel(
            name='Cupon_Aplicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=300)),
                ('estado', models.BooleanField(default=True)),
                ('cupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cupon')),
            ],
        ),
    ]
