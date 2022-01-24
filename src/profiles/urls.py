from django.urls import path
from . import views


urlpatterns = [
    path("my/profile/<int:pk>/", views.UserNewPrivatView.as_view({'get': 'retrieve', 'put': 'update'})),
    path("public/profile/<int:pk>/", views.UserNewPublicView.as_view({'get': 'retrieve'})),
    path("update/avatar/<int:pk>/", views.UserNewAvatarUpdateView.as_view()),
]