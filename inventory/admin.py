from django.contrib import admin
from inventory.models import Inventory, Order, Table, Purchase, Item
# Register your models here.
admin.site.register(Inventory)
admin.site.register(Order)

admin.site.register(Table)
admin.site.register(Item)
admin.site.register(Purchase)


# class StockReportAdmin(admin.ModelAdmin):
#     list_display = ('inventory', 'order', 'stock_remain')

#     def stock_remain(self, obj):
#         return obj.stock_remain


# admin.site.register(StockReport)
