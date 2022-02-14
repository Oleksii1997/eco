from django.urls import path
from . import views


urlpatterns = [
    path('subscribe/', views.EventSubscribeViewSet.as_view({'post': 'create'})),
    path('unsubscribe/<int:pk>', views.EventSubscribeViewSet.as_view({'delete': 'destroy'})),

    path('subscribers/<int:event_id>', views.EventSubscribersListView.as_view())
]