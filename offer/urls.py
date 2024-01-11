from django.urls import path
from . import views
from .views import (
    TrainingsListView,
    TrainingsCreateView,
    TrainingsDeleteView,
    TrainingsDetailView,
    TrainingsUpdateView,
    OffersDeleteView,
    OffersCreateView,
    OffersDetailView,
    OffersUpdateView,
    OffersListView,
)

urlpatterns = [
    path("offers/", OffersListView.as_view(), name="offers"),
    path("offers/<int:pk>/", OffersDetailView.as_view(), name="offers_details"),
    path("offers/new/", OffersCreateView.as_view(), name="offers_add"),
    path("offers/<int:pk>/update/", OffersUpdateView.as_view(), name="offers_update"),
    path("offers/<int:pk>/delete/", OffersDeleteView.as_view(), name="offers_delete"),
    path("trainings/", TrainingsListView.as_view(), name="trainings"),
    path(
        "trainings/<int:pk>/", TrainingsDetailView.as_view(), name="trainings_details"
    ),
    path("trainings/new/", TrainingsCreateView.as_view(), name="trainings_add"),
    path(
        "trainings/<int:pk>/update/",
        TrainingsUpdateView.as_view(),
        name="trainings_update",
    ),
    path(
        "trainings/<int:pk>/delete/",
        TrainingsDeleteView.as_view(),
        name="trainings_delete",
    ),
]
