from django.urls import path
from . import views

urlpatterns = [path("clients/", views.clients_members, name="clients")]
