from django.urls import path
from .views import SearchView, DishDetailView, DishListView, AddDishView, AddOrderView
app_name = 'coocking_book'
urlpatterns = [
    path('', DishListView.as_view(), name='dish_list'),
    path('dish/<int:pk>', DishDetailView.as_view(), name='dish_detail'),
    path('dish_search/result', SearchView.as_view(), name='dish_search'),
    path('add_dish', AddDishView.as_view(), name='add_dish'),
    path('add_order_list/<int:pk>',
         AddOrderView.as_view(), name='add_order_list'),
]
