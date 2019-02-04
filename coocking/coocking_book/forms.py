from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Dish, Ingredient


class AddIngredientForm(forms.ModelForm):

	class Meta:
		model = Ingredient
		fields = ('name', 'weight')



class AddDishForm(forms.ModelForm):

	class Meta:
		model = Dish
		fields = ('title', 'description')
		exclude = ('ingredient',)




