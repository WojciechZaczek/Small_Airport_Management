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
    HangarsDetailView,
    HangarsCreateView,
    HangarsUpdateView,
    HangarsDeleteView,
    OutsideStandsDetailView,
    OutsideStandsDeleteView,
    OutsideStandsCreateView,
    OutsideStandsUpdateView,
)


urlpatterns = [
    path("airports/", AirportListView.as_view(), name="airports"),
    path(
        "airports/<int:pk>/update/", AirportUpdateView.as_view(), name="airports_update"
    ),
    path("runways/", RunwaysListView.as_view(), name="runways"),
    path("runways/<int:pk>/", RunwaysDetailView.as_view(), name="runways_details"),
    path("runways/new/", RunwaysCreateView.as_view(), name="runways_add"),
    path(
        "runways/<int:pk>/update/", RunwaysUpdateView.as_view(), name="runways_update"
    ),
    path(
        "runways/<int:pk>/delete/", RunwaysDeleteView.as_view(), name="runways_delete"
    ),
    path("aircraft_stands/", views.aircraft_stands, name="aircraft_stands"),
    path("hangars/<int:pk>/", HangarsDetailView.as_view(), name="hangars_details"),
    path("hangars/new/", HangarsCreateView.as_view(), name="hangars_add"),
    path(
        "hangars/<int:pk>/update/", HangarsUpdateView.as_view(), name="hangars_update"
    ),
    path(
        "hangars/<int:pk>/delete/", HangarsDeleteView.as_view(), name="hangars_delete"
    ),
    path(
        "outside-stands/<int:pk>/",
        OutsideStandsDetailView.as_view(),
        name="outside_stands_details",
    ),
    path(
        "outside-stands/new/",
        OutsideStandsCreateView.as_view(),
        name="outside_stands_add",
    ),
    path(
        "outside-stands/<int:pk>/update/",
        OutsideStandsUpdateView.as_view(),
        name="outside_stands_update",
    ),
    path(
        "outside-stands/<int:pk>/delete/",
        OutsideStandsDeleteView.as_view(),
        name="outside_stands_delete",
    ),
]
