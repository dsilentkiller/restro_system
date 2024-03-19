# Generated by Django 5.0.3 on 2024-03-19 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('gm', 'gm'), ('piece', 'piece'), ('ml', 'ml'), ('liter', 'liter'), ('plate', 'plate')], max_length=100)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
                ('item_name', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='menu.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('gm', 'gm'), ('piece', 'piece'), ('ml', 'ml'), ('liter', 'liter'), ('plate', 'plate')], max_length=100)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
                ('item_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('table', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.table')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('gm', 'gm'), ('piece', 'piece'), ('ml', 'ml'), ('liter', 'liter'), ('plate', 'plate')], max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
                ('item_name', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='menu.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='StockReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.order')),
            ],
        ),
    ]
