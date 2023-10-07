from django.urls import path
from . import views
from .views import (
    ClientsListView,
    ClientsDetailView,
    ClientsUpdateView,
    ClientsCreateView,
    ClientsDeleteView,
)

urlpatterns = [
    path("clients/", ClientsListView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientsDetailView.as_view(), name="clients_detail"),
    path("clients/new/", ClientsCreateView.as_view(), name="client_add"),
    path(
        "clients/update/<int:pk>/", ClientsUpdateView.as_view(), name="clients_update"
    ),
    path(
        "clients/delete/<int:pk>/", ClientsDeleteView.as_view(), name="clients_delete"
    ),
]
