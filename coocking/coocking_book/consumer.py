from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class DishUpdateConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "coocking_book_clients", self.channel_name)
        self.accept()

    def update_message(self, event):
        self.send(text_data=event["text_data"])

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "coocking_book_clients", self.channel_name)
