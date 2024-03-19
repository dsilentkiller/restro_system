from django.contrib import admin
from inventory.models import Inventory, Order, Category, Table, StockReport, Purchase
# Register your models here.
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(StockReport)
admin.site.register(Purchase)
