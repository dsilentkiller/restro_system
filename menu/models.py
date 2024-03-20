from django.db import models

CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Receipe(models.Model):
    name = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    unit = models.CharField(choices=CHOICES, max_length=100, null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.unit}'


class MenuItem(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)

    price = models.FloatField(null=True)
    # image = models.ImageField(upload_to='static', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    receipe = models.ManyToManyField(
        Receipe)

    def __str__(self):
        return self.name
