from django.urls import path
from . import views
from .views import (
    NotificationsCreateView,
    NotificationsDeleteView,
    NotificationsDetailView,
    NotificationsUpdateView,
)

urlpatterns = [
    path("notifications/", views.notifications, name="notifications"),
    path(
        "notifications/<int:pk>/",
        NotificationsDetailView.as_view(),
        name="notifications_details",
    ),
    path(
        "notifications/new/",
        NotificationsCreateView.as_view(),
        name="notifications_add",
    ),
    path(
        "notifications/update/<int:pk>/",
        NotificationsUpdateView.as_view(),
        name="notifications_update",
    ),
    path(
        "notifications/delete/<int:pk>/",
        NotificationsDeleteView.as_view(),
        name="notifications_delete",
    ),
]
