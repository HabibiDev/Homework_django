from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from coocking_book.auth_token import TokenAuthMiddlewareStack
from coocking_book.consumer import DishUpdateConsumer
from coocking_book import routing

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        ),
    ),
})
