from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import CreatClients
from airport.models import Airport


@method_decorator(login_required, name="dispatch")
class ClientsListView(ListView):
    model = Client
    template_name = "clients/clients.html"
    context_object_name = "clients"

    def get_queryset(self):
        user = self.request.user
        clients = Client.objects.filter(company_id=user.company_id)
        return clients


class ClientsDetailView(DetailView):
    model = Client
    template_name = "clients/clients_detail.html"


@method_decorator(login_required, name="dispatch")
class ClientsCreateView(CreateView):
    model = Client
    template_name = "clients/clients_form.html"
    form_class = CreatClients

    def form_valid(self, form):
        company_id = self.request.user.company_id
        form.instance.company_id = company_id
        return super().form_valid(form)


class ClientsUpdateView(UpdateView):
    model = Client
    template_name = "clients/clients_form.html"

    form_class = CreatClients


class ClientsDeleteView(DeleteView):
    model = Client
    template_name = "clients/clients_delete.html"
    success_url = reverse_lazy("clients")
