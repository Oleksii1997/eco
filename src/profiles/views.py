from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import UserNew
from .serializers import GetUserNewSerializer, GetUserNewPublicSerializer


class UserNewPublicView(ModelViewSet):
    """Вивід публічного профеля користувача"""
    queryset = UserNew.objects.all()
    serializer_class = GetUserNewPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNewView(ModelViewSet):
    """Вивід профелю користувача (приватний)"""
    serializer_class = GetUserNewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNew.objects.filter(id=self.request.user.id)
