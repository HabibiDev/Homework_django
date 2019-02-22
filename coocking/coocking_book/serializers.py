from rest_framework import serializers
from .models import Dish, Order


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ('id', 'title', 'description', 'author')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'contact', 'order_date', 'is_active', 'dish', 'author')
