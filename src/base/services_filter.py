from django_filters import rest_framework as filters
from src.event.models import Event


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """Для реалізації можливості фільтрації по назві"""
    pass


class EventFilter(filters.FilterSet):
    """Фільтрація подій по категоріям, містам та формату проведення"""

    category = CharFilterInFilter(field_name="category__name", lookup_expr="in")
    city = CharFilterInFilter(field_name="city__name", lookup_expr="in")
    event_format = filters.ChoiceFilter(choices=Event.EVENT_FORMAT)

    class Meta:
        model = Event
        fields = ['category', 'city', 'event_format']