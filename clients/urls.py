from django.urls import path
from . import views
from .views import (
    ClientsListView,
    ClientsDetailView,
    ClientsUpdateView,
    ClientsCorporateCreateView,
    ClientsPrivateCreateView,
    ClientsDeleteView,
)

urlpatterns = [
    path("clients/", ClientsListView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientsDetailView.as_view(), name="clients_details"),
    path("clients/new/", views.new_client, name="clients_add"),
    path(
        "clients/new/private",
        ClientsPrivateCreateView.as_view(),
        name="clients_add_private",
    ),
    path(
        "clients/new/corporate",
        ClientsCorporateCreateView.as_view(),
        name="clients_add_corporate",
    ),
    path(
        "clients/<int:pk>/update/", ClientsUpdateView.as_view(), name="clients_update"
    ),
    path(
        "clients/<int:pk>/delete/", ClientsDeleteView.as_view(), name="clients_delete"
    ),
]
