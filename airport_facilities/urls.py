from django.urls import path
from . import views

urlpatterns = [
    path("buildings/", views.buildings, name="buildings"),
    path("other_facilities/", views.other_facilities, name="other_facilities"),
]
