from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Client
from .forms import CreatClients


class ClientsListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/clients.html"
    context_object_name = "clients"

    def get_queryset(self):
        user = self.request.user
        clients = Client.objects.filter(company=user.company)
        return clients


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/clients_details.html"


@login_required()
def new_client(request):
    return render(request, "clients/clients_new.html", {"title": "New Client"})


class ClientsCorporateCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/clients_corporate_form.html"
    form_class = CreatClients

    def form_valid(self, form):
        company = self.request.user.company
        form.instance.company = company
        form.instance.corporate_client = True
        return super().form_valid(form)


class ClientsPrivateCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/clients_private_form.html"
    form_class = CreatClients

    def form_valid(self, form):
        company = self.request.user.company
        form.instance.company = company
        form.instance.corporate_client = False

        return super().form_valid(form)

    def form_invalid(self, form):
        form.is_valid()
        print(form.errors)
        return render(
            self.request, self.template_name, {"form": form, "title": "New Client"}
        )


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "clients/clients_form.html"

    form_class = CreatClients


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "clients/clients_delete.html"
    success_url = reverse_lazy("clients")
