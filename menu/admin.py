from django.contrib import admin
from menu.models import Ingredient, Receipe, MenuItem,Category
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Receipe)
admin.site.register(Category)
