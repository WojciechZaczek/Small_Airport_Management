from django.urls import path
from . import views

urlpatterns = [path("aircrafts/", views.aircraft, name="aircrafts")]
