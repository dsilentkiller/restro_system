from django.db import models
from inventory.models import Category
CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),)


class Receipe(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    unit = models.CharField(choices=CHOICES, max_length=100, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField()
    # image = models.ImageField(upload_to='static', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    receipe = models.ManyToManyField(
        Receipe)

    def __str__(self):
        return self.name
