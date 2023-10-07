from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Building, Others, Property, Vehicle
from .forms import CreateBuilding, CreateVehicle, CreateProperty, CreateOthers
from airport.models import Airport


class BuildingsListView(LoginRequiredMixin, ListView):
    model = Building
    template_name = "airport_facilities/buildings.html"
    context_object_name = "buildings"

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company_id)
        trainings = Building.objects.filter(airport_id__in=airports)

        return trainings


class BuildingsDetailView(LoginRequiredMixin, DetailView):
    model = Building
    template_name = "airport_facilities/buildings_details.html"


class BuildingsCreateView(LoginRequiredMixin, CreateView):
    model = Building
    template_name = "airport_facilities/buildings_form.html"

    form_class = CreateBuilding


class BuildingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Building
    template_name = "airport_facilities/buildings_form.html"

    form_class = CreateBuilding


class BuildingsDeleteView(DeleteView):
    model = Building
    template_name = "airport_facilities/buildings_delete.html"
    success_url = reverse_lazy("buildings")


def other_facilities(request):
    return render(
        request,
        "airport_facilities/other_facilities.html",
        {"title": "Other facilities"},
    )


class VehiclesDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_details.html"


class VehiclesCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_form.html"

    form_class = CreateVehicle


class VehiclesUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_form.html"

    form_class = CreateVehicle


class VehiclesDeleteView(DeleteView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_delete.html"
    success_url = reverse_lazy("other_facilities")


class PropertiesDetailView(LoginRequiredMixin, DetailView):
    model = Property
    template_name = "airport_facilities/properties_details.html"


class PropertiesCreateView(LoginRequiredMixin, CreateView):
    model = Property
    template_name = "airport_facilities/properties_form.html"

    form_class = CreateProperty


class PropertiesUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    template_name = "airport_facilities/properties_form.html"

    form_class = CreateProperty


class PropertiesDeleteView(DeleteView):
    model = Property
    template_name = "airport_facilities/properties_delete.html"
    success_url = reverse_lazy("other_facilities")


class OthersDetailView(LoginRequiredMixin, DetailView):
    model = Others
    template_name = "airport_facilities/others_details.html"


class OthersCreateView(LoginRequiredMixin, CreateView):
    model = Others
    template_name = "airport_facilities/others_form.html"

    form_class = CreateOthers


class OthersUpdateView(LoginRequiredMixin, UpdateView):
    model = Others
    template_name = "airport_facilities/others_form.html"

    form_class = CreateOthers


class OthersDeleteView(DeleteView):
    model = Others
    template_name = "airport_facilities/others_delete.html"
    success_url = reverse_lazy("other_facilities")
