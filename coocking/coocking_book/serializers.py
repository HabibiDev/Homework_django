from rest_framework import serializers
from .models import Dish, Order, Ingredient, IngredientInOrder
from notes.models import Note, NotesItem


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('content')


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


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'weight')


class IngredientInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientInOrder
        fields = ('name', 'weight')


class DishSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True)
    notes = NoteSerializer(many =True)

    class Meta:
        model = Dish
        fields = ('id', 'title', 'description', 'ingredient', 'author', 'slug', 'notes')


class OrderSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=IngredientInOrder.objects.all())

    class Meta:
        model = Order
        fields = ('id', 'contact', 'order_date',
                  'is_active', 'dish', 'author', 'ingredients', 'slug')
