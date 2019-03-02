from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from coocking_book.auth_token import TokenAuthMiddlewareStack
from coocking_book.consumer import DishUpdateConsumer

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddlewareStack(
        URLRouter([
            path('', DishUpdateConsumer),
        ]),
    ),
})
