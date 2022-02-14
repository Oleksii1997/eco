from django.apps import AppConfig


class EventSubscribersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.event_subscribers'
    verbose_name = "Панель Підписників до подій"