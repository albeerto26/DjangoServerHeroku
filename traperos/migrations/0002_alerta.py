# Generated by Django 2.0.3 on 2018-03-31 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traperos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha_alerta', models.DateField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('trapero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alertas_traperos', to='traperos.Trapero')),
            ],
        ),
    ]
