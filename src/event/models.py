from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from src.profiles.models import UserNew
from src.location.models import City, Region


class EventCategory(MPTTModel):
    """Модель категорій подій MPTT"""
    name = models.CharField(verbose_name="Назва категорій/підкатегорій", max_length=64)
    parent = TreeForeignKey('self', verbose_name="Батьківська категорія", on_delete=models.CASCADE,
                            blank=True, null=True, related_name='children_category')
    slug = models.SlugField(verbose_name="Slug для url", max_length=32, unique=True)
    is_active = models.BooleanField(verbose_name="Активна/неактивна", default=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    """Модель подій"""
    EVENT_FORMAT = (
        ('online', 'Онлайн'),
        ('offline', 'Оффлайн'),
        ('online-offline', 'Змішаний')
    )
    organizer = models.ForeignKey(UserNew, verbose_name="Організатор", on_delete=models.CASCADE, related_name='events')
    name = models.CharField(verbose_name="Назва події", max_length=128)
    category = models.ForeignKey(EventCategory, verbose_name="Категорія", blank=True, null=True,
                                 on_delete=models.SET_NULL, related_name='event_in_category')
    description = models.TextField(verbose_name="Детальний опис події", max_length=1024)
    date_start = models.DateTimeField(verbose_name="Дата початку події")
    date_end = models.DateTimeField(verbose_name="Дата завершення події", blank=True, null=True)
    event_format = models.CharField(verbose_name="Формат проведення події", max_length=24, choices=EVENT_FORMAT,
                                    default='online')
    city = models.ForeignKey(City, verbose_name="Місто", blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='event_in_city')
    auto_confirmation = models.BooleanField(verbose_name="Автоматично підтверджувати участь в події?", default=False)

    is_active = models.BooleanField(verbose_name="Активна/неактивна", default=True)
    created = models.DateTimeField(verbose_name="Дата створення події", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name="Дата останнього оновлення інформації", auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'

    def __str__(self):
        return f"{self.id}"


class EventSocialLink(models.Model):
    """Посилання на події в соціальних мережах"""
    SOCIAL = (('instagram', 'instagram'),
              ('facebook', 'facebook'),
              ('linkedin', 'linkedin'),
              ('wedsite', 'website'),
              ('other', 'other'))
    event = models.ForeignKey(Event, verbose_name="Подія", on_delete=models.CASCADE, related_name="social_link")
    type = models.CharField(verbose_name="Тип соціальної мережі", max_length=16, choices=SOCIAL, default='other')
    link = models.URLField(verbose_name="Посилання на соціальні мережі", max_length=200)

    class Meta:
        verbose_name = 'Соціальна мережа'
        verbose_name_plural = 'Соціальні мережі, які прикріплені до подій'

    def __str__(self):
        return f"{self.id}"


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

