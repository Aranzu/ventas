# Generated by Django 3.1.2 on 2021-06-25 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('num_boleta', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_pro', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemProducto',
            fields=[
                ('id_item', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boleta.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre_cl', models.CharField(max_length=100)),
                ('num_telf', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('boletas', models.ManyToManyField(blank=True, related_name='clientes', to='boleta.Boleta')),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='ItemProductos',
            field=models.ManyToManyField(blank=True, related_name='ItemProductos', to='boleta.ItemProducto'),
        ),
    ]
