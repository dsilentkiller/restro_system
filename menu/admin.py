from django.contrib import admin
from menu.models import Ingredient, Receipe, MenuItem
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Receipe)
