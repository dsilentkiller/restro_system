# Generated by Django 5.0.3 on 2024-03-19 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_menuitem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]