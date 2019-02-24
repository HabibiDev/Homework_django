from rest_framework import serializers
from .models import Dish, Order, Ingredient, IngredientInOrder
from notes.models import Note, NotesItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'content',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'weight')


class IngredientInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientInOrder
        fields = ('id', 'name', 'weight')


class DishSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True)
    notes = NoteSerializer(many=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Dish
        fields = ('id', 'title', 'description',
                  'ingredient', 'author', 'slug', 'notes')


class OrderSerializer(serializers.ModelSerializer):
    ingredients = IngredientInOrderSerializer(many=True)
    notes = NoteSerializer(many=True)
    dish = DishSerializer()
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Order
        fields = ('id', 'contact', 'order_date',
                  'is_active', 'dish', 'author', 'ingredients', 'slug', 'notes')


class NoteTargetField(serializers.Field):
    serializer_map = {
        Dish: DishSerializer,
        Order: OrderSerializer,
    }

    def to_representation(self, obj):
        serializer = self.serializer_map[obj.__class__]
        return serializer.to_representation(obj)


class NoteItemSerializer(serializers.ModelSerializer):
    note = NoteSerializer()
    target_object = NoteTargetField(source='content_object')
