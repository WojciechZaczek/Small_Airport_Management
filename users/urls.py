from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import (
    register,
    login_view,
    UserListView,
    UserDeleteView,
    UserDetailView,
    UserUpdateView,
)


urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("users/", UserListView.as_view(), name="users"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="users_details"),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="users_update"),
    path("users/delete/<int:pk>/", UserDeleteView.as_view(), name="users_delete"),
]
