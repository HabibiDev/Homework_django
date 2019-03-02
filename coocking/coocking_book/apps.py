from django.apps import AppConfig


class Coocking_bookConfig(AppConfig):
    name = 'coocking_book'

    def ready(self):
        import coocking_book.signals
