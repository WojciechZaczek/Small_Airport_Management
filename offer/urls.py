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
    path("offers/update/<int:pk>/", OffersUpdateView.as_view(), name="offers_update"),
    path("offers/delete/<int:pk>/", OffersDeleteView.as_view(), name="offers_delete"),
    path("trainings/", TrainingsListView.as_view(), name="trainings"),
    path("trainings/<int:pk>/", TrainingsDetailView.as_view(), name="trainings_detail"),
    path("trainings/new/", TrainingsCreateView.as_view(), name="trainings_add"),
    path(
        "trainings/update/<int:pk>/",
        TrainingsUpdateView.as_view(),
        name="trainings_update",
    ),
    path(
        "trainings/delete/<int:pk>/",
        TrainingsDeleteView.as_view(),
        name="trainings_delete",
    ),
]
