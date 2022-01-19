from rest_framework import serializers
from .models import UserNew


class GetUserNewSerializer(serializers.ModelSerializer):
    """Вивід інформації про користувача"""

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

