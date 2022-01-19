from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Побудова шляху для завантаження аватара користувача.
    Формат: /media/avatar/user_id/avatar.png
    instance - об'єкт самого користувача;
    file - файл який завантажують"""

    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    """Перевірка розміру файла"""

    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальний розмір файлу {megabyte_limit}MB")