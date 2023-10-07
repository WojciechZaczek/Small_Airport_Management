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
        "buildings/update/<int:pk>/",
        BuildingsUpdateView.as_view(),
        name="buildings_update",
    ),
    path(
        "buildings/delete/<int:pk>/",
        BuildingsDeleteView.as_view(),
        name="buildings_delete",
    ),
    path("other_facilities/", views.other_facilities, name="other_facilities"),
    path("vehicles/<int:pk>/", VehiclesDetailView.as_view(), name="vehicles_details"),
    path("vehicles/new/", VehiclesCreateView.as_view(), name="vehicles_add"),
    path(
        "vehicles/update/<int:pk>/",
        VehiclesUpdateView.as_view(),
        name="vehicles_update",
    ),
    path(
        "vehicles/delete/<int:pk>/",
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
        "properties/update/<int:pk>/",
        PropertiesUpdateView.as_view(),
        name="properties_update",
    ),
    path(
        "properties/delete/<int:pk>/",
        PropertiesDeleteView.as_view(),
        name="properties_delete",
    ),
    path("others/<int:pk>/", OthersDetailView.as_view(), name="others_details"),
    path("others/new/", OthersCreateView.as_view(), name="others_add"),
    path("others/update/<int:pk>/", OthersUpdateView.as_view(), name="others_update"),
    path("others/delete/<int:pk>/", OthersDeleteView.as_view(), name="others_delete"),
]
