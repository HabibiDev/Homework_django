from django.urls import path
from .views import ordering, SearchView, DishDetailView, DishListView, AddDishView, AddIngredientsToDish

urlpatterns = [
    path('', DishListView.as_view(), name='dish_list'),
    path('<int:pk>', DishDetailView.as_view(), name='dish_detail'),
    path('order/<int:dish_id>', ordering, name='ordering'),
    path('dish_search/', SearchView.as_view(), name='dish_search'),
    path('add_dish', AddDishView.as_view(), name='add_dish'),
    path('add_ingredient/<int:dish_id>', AddIngredientsToDish.as_view(), name='add_ingredient'),

]
