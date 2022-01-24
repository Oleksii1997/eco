from rest_framework import serializers
from .models import UserNew


class GetUserNewPrivatSerializer(serializers.ModelSerializer):
    """Вивід інформації про користувача. Приватний профіль"""

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNew
        exclude = (
            "is_staff",
            "is_active",
            "is_superuser",
            "password",
            "last_login",
            "groups",
            "user_permissions"
        )


class GetUserNewPublicSerializer(serializers.ModelSerializer):
    """Вивід публічної інформації про користувача"""

    class Meta:
        model = UserNew
        exclude = (
            "is_staff",
            "is_active",
            "is_superuser",
            "password",
            "last_login",
            "email",
            "phone",
            "groups",
            "user_permissions"
        )


class UserAvatarUpdateSerializer(serializers.ModelSerializer):
    """Редагування аватару користувача"""
    class Meta:
        model = UserNew
        fields = ('avatar', )

