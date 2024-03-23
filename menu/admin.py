from django.contrib import admin
from menu.models import Ingredient, Recipe, MenuItem,Category
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(Category)
