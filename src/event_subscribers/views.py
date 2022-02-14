from rest_framework import viewsets, generics
from rest_framework import permissions
from .models import EventSubscriber
from src.event.models import Event

from .serializers import EventSubscribeSerializer, ListSubscriberSerializer
from src.base.services import EventSubscribersPagination


class EventSubscribeViewSet(viewsets.ModelViewSet):
    """Підписка/відписка користувача до події"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = EventSubscriber.objects.all()
    serializer_class = EventSubscribeSerializer


class EventSubscribersListView(generics.ListAPIView):
    """Вивід списку підписників на подію"""
    permission_classes = [permissions.AllowAny]
    serializer_class = ListSubscriberSerializer
    pagination_class = EventSubscribersPagination

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        event_subscriber = Event.objects.get(id=event_id).subscribers.all()
        return event_subscriber











