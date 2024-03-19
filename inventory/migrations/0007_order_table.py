# Generated by Django 5.0.3 on 2024-03-18 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_order_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.table'),
        ),
    ]
