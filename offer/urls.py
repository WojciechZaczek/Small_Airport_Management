from django.urls import path
from . import views

urlpatterns = [
    path("offers/", views.offer, name="offers"),
    path("trainings/", views.offer, name="trainings"),
]
