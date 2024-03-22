from django.db import models

CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),)


class MenuItemManager(models.Manager):

    # def category(self, category_name):
    #     return self.get_queryset().filter(category_name=category_name)

    def filter_by_quantity(self, quantity):
        return super().get_queryset().filter(receipe_quantity=quantity)


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

    name = models.OneToOneField(
        Ingredient, on_delete=models.CASCADE, max_length=100, null=True, unique=True)
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
    menu_objects = MenuItemManager()

    def __str__(self):
        return self.name

    # def total_receipe_quantity(self):
    #     total_quantity = self.receipe.count()
    #     return total_quantity
