# Generated by Django 3.1 on 2021-01-29 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_auto_20210129_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagoefectivo',
            name='solicitud',
        ),
        migrations.RemoveField(
            model_name='pagotarjeta',
            name='solicitud',
        ),
        migrations.CreateModel(
            name='PagoSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('pago_efectivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.pagoefectivo')),
                ('pago_tarjeta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.pagotarjeta')),
                ('solicitud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.solicitud')),
            ],
        ),
    ]
