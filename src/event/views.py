from rest_framework import generics, filters, viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EventCategorySerializers, ShortInfoEventSerializer, EventDetailSerializer, \
                         EventCreateUpdateSerializer, EventSocialLinkSerializer, EventSubscribeSerializer
from .models import EventCategory, Event, EventSocialLink, EventSubscriber
from src.base.services import EventListSetPagination
from src.base.services_filter import EventFilter


class EventCategoryView(generics.ListAPIView):
    """Вивід списку категорій подій"""
    permission_classes = [permissions.AllowAny]
    queryset = EventCategory.objects.filter(parent=None)
    serializer_class = EventCategorySerializers


class EventListView(generics.ListAPIView):
    """Вивід списку подій"""
    permission_classes = [permissions.AllowAny]
    queryset = Event.objects.filter(is_active=True)
    serializer_class = ShortInfoEventSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering = ['-created']
    filterset_class = EventFilter
    pagination_class = EventListSetPagination


class EventDetailView(viewsets.ReadOnlyModelViewSet):
    """Вивід детальної інформації про подію"""
    permission_classes = [permissions.AllowAny]
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventDetailSerializer


class EventCreateViewSet(viewsets.ModelViewSet):
    """Створення, редагування, видалення подій"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer


class EventSocialLinkCreateViewSet(viewsets.ModelViewSet):
    """Додавання/видалення/редагування посилання на подію в сторонніх ресурсах"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = EventSocialLink.objects.all()
    serializer_class = EventSocialLinkSerializer


class EventSubscribeViewSet(viewsets.ModelViewSet):
    """Підписка/відписка користувача до події"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = EventSubscriber.objects.all()
    serializer_class = EventSubscribeSerializer
