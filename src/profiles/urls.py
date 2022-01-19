from django.urls import path
from . import views


urlpatterns = [
    path("profile/<int:pk>/", views.UserNewView.as_view({'get': 'retrieve', 'put': 'update'})),
    path("<int:pk>/", views.UserNewPublicView.as_view({'get': 'retrieve'})),
]