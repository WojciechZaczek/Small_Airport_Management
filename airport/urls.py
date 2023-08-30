from django.urls import path
from . import views
from .views import (
    RunwaysListView,
    RunwaysDetailView,
    RunwaysCreateView,
    RunwaysUpdateView,
    RunwaysDeleteView,
    AirportListView,
    AirportUpdateView,
)


urlpatterns = [
    path("airports/", AirportListView.as_view(), name="airports"),
    path(
        "airports/update/<int:pk>/", AirportUpdateView.as_view(), name="airports_update"
    ),
    path("runways/", RunwaysListView.as_view(), name="runways"),
    path("runways/<int:pk>/", RunwaysDetailView.as_view(), name="runways_detail"),
    path("runways/new/", RunwaysCreateView.as_view(), name="runways_add"),
    path(
        "runways/update/<int:pk>/", RunwaysUpdateView.as_view(), name="runways_update"
    ),
    path(
        "runways/delete/<int:pk>/", RunwaysDeleteView.as_view(), name="runways_delete"
    ),
]
