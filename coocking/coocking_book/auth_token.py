from channels.auth import AuthMiddlewareStack
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from rest_framework.authtoken.models import Token


class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        try:
            token_name, token_key = scope['query_string'].decode().split('=')
            if token_name == 'Token':
                token = Token.objects.get(key=token_key)
                scope['user'] = token.user
        except Token.DoesNotExist:
            scope['user'] = AnonymousUser()
        return self.inner(scope)


def TokenAuthMiddlewareStack(inner): return TokenAuthMiddleware(
    AuthMiddlewareStack(inner))
