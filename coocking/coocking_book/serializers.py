from rest_framework import serializers
from .models import Dish, Order, Ingredient, IngredientInOrder


class DishSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredient.objects.all())

    class Meta:
        model = Dish
        fields = ('id', 'title', 'description', 'ingredient', 'author', 'slug')


class OrderSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=IngredientInOrder.objects.all())

    class Meta:
        model = Order
        fields = ('id', 'contact', 'order_date',
                  'is_active', 'dish', 'author', 'ingredients', 'slug')
