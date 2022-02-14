from django.db import models
from src.event.models import Event
from src.profiles.models import UserNew


class EventSubscriber(models.Model):
    """Підписники до подій"""
    event = models.ForeignKey(Event, verbose_name="Подія", on_delete=models.CASCADE, related_name='subscribers')
    user = models.ForeignKey(UserNew, verbose_name="Підписник", on_delete=models.CASCADE, related_name='my_subscribe')
    confirmation = models.BooleanField(verbose_name="Участь в події підтверджена організатором?", default=False)
    created = models.DateTimeField(verbose_name="Дата створення події", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Учасник події'
        verbose_name_plural = 'Учасники подій'

    def __str__(self):
        return f"{self.id}"