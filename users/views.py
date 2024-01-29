from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

from django.contrib.auth.views import LoginView

from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CreateUser


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Invalid username or password.",
        )
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


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
    success_url = reverse_lazy("users")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "users/users_form.html"
    form_class = CreateUser
