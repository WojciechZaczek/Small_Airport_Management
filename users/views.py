from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CreateUser


def login_view(request):
    form = UserLoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "users/login.html", {"form": form, "msg": msg})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Dear {username} you have been successfully signed up!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/users.html"
    context_object_name = "users"

    def get_queryset(self):
        user = self.request.user
        users = CustomUser.objects.filter(company=user.company)
        return users


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/users_details.html"


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "users/users_delete.html"
    success_url = reverse_lazy("user js")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "users/users_form.html"
    form_class = CreateUser
