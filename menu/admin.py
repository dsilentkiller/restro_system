from django.contrib import admin
from menu.models import MenuItem, Receipe, Ingredient
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Receipe)
