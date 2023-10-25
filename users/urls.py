from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import register, login_view


urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
]
