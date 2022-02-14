from rest_framework import serializers
from .models import EventSubscriber
from src.profiles.serializers import ShortUserNewPublicProfileSerializer


class EventSubscribeSerializer(serializers.ModelSerializer):
    """Серіалізатор для підписки/відписки користувачів"""

    class Meta:
        model = EventSubscriber
        fields = ('id', 'event', 'user', 'confirmation')

    def create(self, validated_data):
        rating, _ = EventSubscriber.objects.update_or_create(
            event=validated_data.get('event', None),
            user=validated_data.get('user', None),
            defaults={'confirmation': validated_data.get('event', None).auto_confirmation}
        )
        return rating


class ListSubscriberSerializer(serializers.ModelSerializer):
    """Серіалізація підписників на подію"""
    user = ShortUserNewPublicProfileSerializer(read_only=True)

    class Meta:
        model = EventSubscriber
        fields = ('user', 'confirmation')