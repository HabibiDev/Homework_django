from django.contrib import admin
from .models import Dish, Ingredient, Order, IngredientInOrder

# Register your models here.


class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title',)
    fields = ['title', 'description', 'ingredient']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight',)
    list_filter = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('contact', 'dish', 'author', 'is_active')
    

admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(IngredientInOrder)
