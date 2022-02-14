from django.core.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


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


class EventListSetPagination(PageNumberPagination):
    """Пагінатор списку подій"""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):

        return Response(
            {
                "links": {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            }
        )


class EventSubscribersPagination(PageNumberPagination):
    """Пагінатор підписників на подію"""
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):

        return Response(
            {
                "links": {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            }
        )

