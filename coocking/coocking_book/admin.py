from django.contrib import admin
from .models import Dish, Ingredient

# Register your models here.


class DishAdmin(admin.ModelAdmin):

	list_filter = ('title', 
                   )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')
    list_filter = ('name',)



admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
