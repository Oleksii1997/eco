from rest_framework import generics
from rest_framework import permissions
from .serializers import CityListSerializers
from .models import City

from django_filters import rest_framework as rest_filters
from rest_framework import filters


class CityListView(generics.ListAPIView):
    """Вивід населених пунктів"""
    permission_classes = [permissions.AllowAny]
    queryset = City.objects.all()
    serializer_class = CityListSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'region__name']


