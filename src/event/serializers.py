from rest_framework import serializers
from .models import EventCategory, Event, EventSocialLink
from src.profiles.serializers import ShortUserNewPublicProfileSerializer
from src.location.serializers import CityListSerializers
from src.event_subscribers.serializers import ListSubscriberSerializer


class FilterCategoryListSerializers(serializers.ListSerializer):
    """Фільтр ктегорій, для виводу тільки батьківських"""
    def to_representation(self, data):
        data = data.filter(parant=None)
        return super().to_representation(data)


class RecursiveSerializers(serializers.Serializer):
    """Рекурсивний вивід вкладених категорій подій"""

    def to_representation(self, value):
        serializers = self.parent.parent.__class__(value, context=self.context)
        return serializers.data


class EventCategorySerializers(serializers.ModelSerializer):
    """Серіалізація категорій подій"""
    children_category = RecursiveSerializers(many=True)

    class Meta:
        list_serialize_class = FilterCategoryListSerializers
        model = EventCategory
        fields = ('name', 'slug', 'children_category')


class CategoryNameSerializer(serializers.ModelSerializer):
    """Серіалізація назви категорії для її виводу в складі списку подій"""

    class Meta:
        model = EventCategory
        fields = ('name',)


class EventSocialLinkSerializer(serializers.ModelSerializer):
    """Серіалізатор посиланнь на обрану подію"""

    class Meta:
        model = EventSocialLink
        fields = ('id', 'event', 'type', 'link')


class ShortInfoEventSerializer(serializers.ModelSerializer):
    """Серіалізація короткої інформації про подію
    при виводу списку подій"""
    organizer = ShortUserNewPublicProfileSerializer()
    city = CityListSerializers()
    category = CategoryNameSerializer()

    class Meta:
        model = Event
        fields = ('id',
                  'organizer',
                  'name',
                  'category',
                  'date_start',
                  'date_end',
                  'event_format',
                  'city',
                  'auto_confirmation',
                  'created')


class EventDetailSerializer(serializers.ModelSerializer):
    """Вивід детальної інформації про подію"""
    organizer = ShortUserNewPublicProfileSerializer()
    city = CityListSerializers()
    category = CategoryNameSerializer()
    social_link = EventSocialLinkSerializer(many=True, read_only=True)
    count_subscribers = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = ('id',
                  'count_subscribers',
                  'organizer',
                  'name',
                  'category',
                  'description',
                  'social_link',
                  'date_start',
                  'date_end',
                  'event_format',
                  'city',
                  'auto_confirmation',
                  'is_active',
                  'created')


class EventCreateUpdateSerializer(serializers.ModelSerializer):
    """Серіалізатор для створення/оновлення події"""

    class Meta:
        model = Event
        fields = ('id',
                  'organizer',
                  'name',
                  'category',
                  'description',
                  'date_start',
                  'date_end',
                  'event_format',
                  'city',
                  'auto_confirmation',
                  'is_active')


