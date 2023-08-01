from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import register, login_view


urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
