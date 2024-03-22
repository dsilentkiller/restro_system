from django.db import models
from menu.models import Ingredient, Category, MenuItem

CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),
           ('plate', 'plate'),)


class InventoryManager(models.Manager):

    # def category(self, category_name):
    #     return self.get_queryset().filter(category_name=category_name)

    def filter_by_quantity(self, quantity):
        return self.get_queryset().filter(quantity=quantity)


class Table(models.Model):
    name = models.CharField(max_length=50)
    floor = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, max_length=100)
    quantity = models.FloatField()
    price = models.FloatField()
    unit = models.CharField(choices=CHOICES, max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # vendor=models.ForeignKey(vendor)

    def __str__(self):
        return self.item_name


class Inventory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, max_length=100)
    quantity = models.FloatField()
    price = models.FloatField()
    unit = models.CharField(choices=CHOICES, max_length=100)
    description = models.TextField()
    inventory_objects = InventoryManager()
    # vendor=models.ForeignKey(vendor)

    def __str__(self):
        return f'{self.item_name}-{self.category}'


class Order(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu_item_name = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, max_length=100, null=True)
    quantity = models.FloatField()
    price = models.FloatField()
    unit = models.CharField(choices=CHOICES, max_length=100)
    remark = models.TextField(null=True)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, max_length=100, null=True)
    # vendor=models.ForeignKey(vendor)

    def __str__(self):
        return f'{self.menu_item_name}-{self.category}'

    # def calculate_stock(self):
    #     stock= self.inventory.quantity-order.quantity)

    def stock(request):
        inventory = Inventory.inventory_objects.all()
        print(inventory)

    def calculate(request):
        inventory_quantity = Inventory.inventory_objects.filter_by_name(10)
        menu_quantity = MenuItem.menu_objects.filter_by_quantity(10)
        total = inventory_quantity - menu_quantity
        return total
    




# class StockReport(models.Model):
#     menu_item_name = models.ForeignKey(
#         MenuItem, on_delete=models.CASCADE, null=True)
#     inventory_quantity = models.ForeignKey(
#         Inventory, on_delete=models.CASCADE, null=True)
#     order_quantity = models.ForeignKey(
#         Order, on_delete=models.CASCADE, null=True)
#     stock_remain = models.FloatField(null=True)

    # def calculate(request):
    #     inventory_quantity = Inventory.inventory_objects.filter_by_quantity(10)
    #     menu_quantity = MenuItem.menu_objects.filter_by_quantity(10)
    #     total = inventory_quantity - menu_quantity
    #     return total

    # def __str__(self):
    #     return f'{self.menu_item_name}-{self.inventory}-{self.order}-{self.stock_remain}'
# when  order is done, inventory quantity-receipe quantity  =result

    # def update_total(self):
    #     receipe_total = self.menu_item_name.total
    #     inventory_total = self.inventory_quantity.total
    #     stock = inventory_total - receipe_total
    #     self.total = stock
    #     self.save()
    #     return stock
