from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from .models import Dish, Ingredient, Order, OrderIngredients


class AddIngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'weight')


AddIngredientFormFormSet = formset_factory(
    AddIngredientForm, extra=10, min_num=1)


class AddDishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('title', 'description')
        exclude = ('ingredient',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('contact',)
        exclude = ('order_date', 'dish')

class OrderIngredientsForm(forms.ModelForm):
    class Meta:
        model = OrderIngredients
        fields = ('quantity',)
        exclude = ('order', 'ingredients',)


    



AddIngredientToOrderFormSet = modelformset_factory(
    Ingredient, form = AddIngredientForm, fields=('name', 'weight',))
