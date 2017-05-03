from django.apps import AppConfig


class AvacatappConfig(AppConfig):
    name = 'avacatapp'
    def ready(self):
        import avacatapp.signals  # noqa
