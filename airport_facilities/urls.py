from django.urls import path
from . import views
from .views import (
    BuildingsDeleteView,
    BuildingsUpdateView,
    BuildingsListView,
    BuildingsCreateView,
    BuildingsDetailView,
    VehiclesDeleteView,
    VehiclesCreateView,
    VehiclesDetailView,
    VehiclesUpdateView,
    PropertiesCreateView,
    PropertiesDeleteView,
    PropertiesDetailView,
    PropertiesUpdateView,
    OthersDeleteView,
    OthersDetailView,
    OthersCreateView,
    OthersUpdateView,
)

urlpatterns = [
    path("buildings/", BuildingsListView.as_view(), name="buildings"),
    path(
        "buildings/<int:pk>/", BuildingsDetailView.as_view(), name="buildings_details"
    ),
    path("buildings/new/", BuildingsCreateView.as_view(), name="buildings_add"),
    path(
        "buildings/<int:pk>/update/",
        BuildingsUpdateView.as_view(),
        name="buildings_update",
    ),
    path(
        "buildings/<int:pk>/delete/",
        BuildingsDeleteView.as_view(),
        name="buildings_delete",
    ),
    path("other-facilities/", views.other_facilities, name="other_facilities"),
    path("vehicles/<int:pk>/", VehiclesDetailView.as_view(), name="vehicles_details"),
    path("vehicles/new/", VehiclesCreateView.as_view(), name="vehicles_add"),
    path(
        "vehicles/<int:pk>/update/",
        VehiclesUpdateView.as_view(),
        name="vehicles_update",
    ),
    path(
        "vehicles/<int:pk>/delete/",
        VehiclesDeleteView.as_view(),
        name="vehicles_delete",
    ),
    path(
        "properties/<int:pk>/",
        PropertiesDetailView.as_view(),
        name="properties_details",
    ),
    path("properties/new/", PropertiesCreateView.as_view(), name="properties_add"),
    path(
        "properties/<int:pk>/update/",
        PropertiesUpdateView.as_view(),
        name="properties_update",
    ),
    path(
        "properties/<int:pk>/delete/",
        PropertiesDeleteView.as_view(),
        name="properties_delete",
    ),
    path("others/<int:pk>/", OthersDetailView.as_view(), name="others_details"),
    path("others/new/", OthersCreateView.as_view(), name="others_add"),
    path("others/<int:pk>/update/", OthersUpdateView.as_view(), name="others_update"),
    path("others/<int:pk>/delete/", OthersDeleteView.as_view(), name="others_delete"),
]
