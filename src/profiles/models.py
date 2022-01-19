from django.db import models
from django.core.validators import FileExtensionValidator
from src.base.services import get_path_upload_avatar, validate_size_image
from django.contrib.auth.models import AbstractUser


class UserNew(AbstractUser):
    """Модель користувачів"""
    GENDER_CHOICE = (("man", "Чоловіча"),
                     ("female", "Жіноча"))
    avatar = models.ImageField(verbose_name="Аватар",
                               upload_to=get_path_upload_avatar,
                               blank=True,
                               null=True,
                               validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']),
                                           validate_size_image])
    gender = models.CharField(verbose_name="Стать", max_length=16, choices=GENDER_CHOICE)
    bio = models.TextField(verbose_name="Про мене", max_length=1000, blank=True)
    phone = models.CharField(verbose_name="Номер телефону", max_length=16, unique=True)
    birthday = models.DateField(verbose_name="Дата народження", blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class SocialLink(models.Model):
    """Модель соціальних мереж користувачів"""
    user = models.ForeignKey(UserNew, verbose_name="Користувач", on_delete=models.CASCADE, related_name='social_link')
    link = models.URLField(verbose_name="Посилання", max_length=150)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = "Соціальна мережа"
        verbose_name_plural = "Соціальні мережі користувачів"
