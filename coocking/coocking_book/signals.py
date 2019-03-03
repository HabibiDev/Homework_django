from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from django.conf import settings
from .models import Dish
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Dish)
def update_dish_message(sender, instance=None, created=False, **kwargs):
    async_to_sync(channel_layer.group_send)("coocking_book_clients", {
        "type": "update.message",
        "text_data": 'Reload'})
    print('update_dish_list')
