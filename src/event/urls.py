from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.EventCategoryView.as_view()),
    path('list_event/', views.EventListView.as_view()),
    path('some_event/<int:pk>', views.EventDetailView.as_view({'get': 'retrieve'})),

    path('create/', views.EventCreateViewSet.as_view({'post': 'create'})),
    path('update/<int:pk>', views.EventCreateViewSet.as_view({'put': 'update'})),
    path('delete/<int:pk>', views.EventCreateViewSet.as_view({'delete': 'destroy'})),

    path('link/create', views.EventSocialLinkCreateViewSet.as_view({'post': 'create'})),
    path('link/update/<int:pk>', views.EventSocialLinkCreateViewSet.as_view({'put': 'update'})),
    path('link/delete/<int:pk>', views.EventSocialLinkCreateViewSet.as_view({'delete': 'destroy'})),
]