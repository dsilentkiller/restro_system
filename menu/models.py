from django.db import models


CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    food_name = models.CharField(max_length=200, null=True, unique=True)
    price = models.FloatField(null=True)

    # receipe = models.ManyToManyField(
    #     Receipe,null=True)

    def __str__(self):
        return f'{self.category}-{self.food_name}-{self.price}'

    # def total_receipe_quantity(self):
    #     total_quantity = self.receipe.count()
    #     return total_quantity


class Recipe(models.Model):
    food_name = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, null=True)

    ingredient_name = models.OneToOneField(
        Ingredient, on_delete=models.CASCADE, max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    unit = models.CharField(choices=CHOICES, max_length=100, null=True)

    def __str__(self):
        return f'{self.food_name}-{self.ingredient_name}-{self.quantity}-{self.unit}'
