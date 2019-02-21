from .models import Dish, Order
from .serializers import DishSerializer, OrderSerializer
from rest_framework import generics


class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
