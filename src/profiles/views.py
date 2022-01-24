from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import UserNew
from .serializers import GetUserNewPrivatSerializer, GetUserNewPublicSerializer, UserAvatarUpdateSerializer


class UserNewPublicView(ModelViewSet):
    """Вивід публічного профеля користувача"""
    queryset = UserNew.objects.all()
    serializer_class = GetUserNewPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNewPrivatView(ModelViewSet):
    """Вивід профелю користувача (приватний)"""
    serializer_class = GetUserNewPrivatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNew.objects.filter(id=self.request.user.id)


class UserNewAvatarUpdateView(generics.UpdateAPIView):
    """Редагування аватару користувача"""

    permission_classes = [permissions.IsAuthenticated]
    queryset = UserNew.objects.all()
    serializer_class = UserAvatarUpdateSerializer

