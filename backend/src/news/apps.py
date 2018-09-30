from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = 'Уведомления и FAQ'

    def ready(self):
        import news.signals
