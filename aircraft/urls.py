from django.urls import path
from . import views
from .views import (
    AircraftsDetailView,
    AircraftsDeleteView,
    AircraftsUpdateView,
    AircraftsCreateView,
    AircraftsHangaredDetailView,
    AircraftsHangaredCreateView,
    AircraftsHangaredDeleteView,
    AircraftsHangaredUpdateView,
)

urlpatterns = [
    path("aircrafts/", views.aircraft, name="aircrafts"),
    path(
        "aircrafts/<int:pk>/", AircraftsDetailView.as_view(), name="aircrafts_details"
    ),
    path("aircrafts/new/", AircraftsCreateView.as_view(), name="aircrafts_add"),
    path(
        "aircrafts/<int:pk>/update/",  # aircrafts/<int:pk>/update/
        AircraftsUpdateView.as_view(),
        name="aircrafts_update",
    ),
    path(
        "aircrafts/<int:pk>/delete/",
        AircraftsDeleteView.as_view(),
        name="aircrafts_delete",
    ),
    path(
        "aircrafts-hangared/<int:pk>/",  # -
        AircraftsHangaredDetailView.as_view(),
        name="aircrafts_hangared_details",
    ),
    path(
        "aircrafts-hangared/new/",
        AircraftsHangaredCreateView.as_view(),
        name="aircrafts_hangared_add",
    ),
    path(
        "aircrafts-hangared/<int:pk>/update/",
        AircraftsHangaredUpdateView.as_view(),
        name="aircrafts_hangared_update",
    ),
    path(
        "aircrafts-hangared/<int:pk>/delete/",
        AircraftsHangaredDeleteView.as_view(),
        name="aircrafts_hangared_delete",
    ),
]
