from .models import Dish, Order
from .serializers import DishSerializer, OrderSerializer
from rest_framework import generics, renderers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response



class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    paginathion_class = LimitOffsetPagination


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    paginathion_class = LimitOffsetPagination


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class DishViewSet(viewsets.ModelViewSet):

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    paginathion_class = LimitOffsetPagination

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        dish = self.get_object()
        return Response(dish.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    paginathion_class = LimitOffsetPagination

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        order = self.get_object()
        return Response(order.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
