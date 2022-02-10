from rest_framework import serializers
from .models import City


class CityListSerializers(serializers.ModelSerializer):
    """Серіалізація населених пунктів"""
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'region')
