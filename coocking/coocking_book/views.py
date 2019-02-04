from django.shortcuts import render, redirect
from .models import Dish, Ingredient
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views import View
from .forms import AddDishForm, AddIngredientForm

# Create your views here.


class DishListView(ListView):

    model = Dish
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_list'] = Dish.objects.all()
        return context


class DishDetailView(DetailView):

    model = Dish
    template_name = 'dish_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DishDetailView, self).get_context_data(**kwargs)
        context['dishes'] = self.model.objects.all()
        context['dish'] = self.get_object()
        context['dishes_ingredients'] = self.get_object().ingredient.all()
        return context


class AddDishView(View):
    template_name = 'add_dish.html'

    def get(self, request, *args, **kwargs):
        form_dish = AddDishForm()
        context = {'form_dish': form_dish}
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_dish = AddDishForm(request.POST)
        context = {'form_dish': form_dish}
        if form_dish.is_valid():
            dish = form_dish.save(commit = False)
            dish.save()
            return redirect('add_ingredient', dish_id = dish.id)
        return render(self.request, self.template_name, context)

class AddIngredientsToDish(View):
    template_name = 'add_ingredient.html'

    def get(self, request, *args, **kwargs):
        form_ingredient = AddIngredientForm()
        new_dish = Dish.objects.get(id = self.kwargs['dish_id'])
        context = {'form_ingredient': form_ingredient, 'new_dish':new_dish, 'dish_id':self.kwargs['dish_id']}
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_ingredient = AddIngredientForm(request.POST)
        new_dish = Dish.objects.get(id = self.kwargs['dish_id'])
        context = {'form_ingredient': form_ingredient, 'new_dish':new_dish, 'dish_id':self.kwargs['dish_id']}
        if form_ingredient.is_valid():
            ingredient = form_ingredient.save(commit = False)
            ingredient.save()
            new_dish.ingredient.add(ingredient)
            new_dish.save()
            return redirect('add_ingredient', dish_id = new_dish.id)
        return render(self.request, self.template_name, context)


def ordering(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    ingredients = Ingredient.objects.filter(dishes=dish_id)
    context = {'dish': dish, 'ingredients': ingredients}
    return render(request, 'ordering.html', context)


class SearchView(ListView):
    model = Dish
    template_name = 'search_result.html'

    def get_queryset(self):
        queryset = super(DishListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(Q(title__icontains=q) |
                                   Q(description__icontains=q))
        return queryset
