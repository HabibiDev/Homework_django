from django.conf.urls import url

from .consumer import DishUpdateConsumer

websocket_urlpatterns = [
    url(r'ws/dishes/', DishUpdateConsumer),
]
