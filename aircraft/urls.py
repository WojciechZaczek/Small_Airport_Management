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
        "aircrafts/update/<int:pk>/",
        AircraftsUpdateView.as_view(),
        name="aircrafts_update",
    ),
    path(
        "aircrafts/delete/<int:pk>/",
        AircraftsDeleteView.as_view(),
        name="aircrafts_delete",
    ),
    path(
        "aircrafts_hangared/<int:pk>/",
        AircraftsHangaredDetailView.as_view(),
        name="aircrafts_hangared_details",
    ),
    path(
        "aircrafts_hangared/new/",
        AircraftsHangaredCreateView.as_view(),
        name="aircrafts_hangared_add",
    ),
    path(
        "aircrafts_hangared/update/<int:pk>/",
        AircraftsHangaredUpdateView.as_view(),
        name="aircrafts_hangared_update",
    ),
    path(
        "aircrafts_hangared/delete/<int:pk>/",
        AircraftsHangaredDeleteView.as_view(),
        name="aircrafts_hangared_delete",
    ),
]
