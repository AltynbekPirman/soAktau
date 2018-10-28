from django.apps import AppConfig


class MyCityConfig(AppConfig):
    name = 'my_city'
    verbose_name = 'Мой Город'

    def ready(self):
        import my_city.signals