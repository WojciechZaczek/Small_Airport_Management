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
        airports = Airport.objects.filter(company_id=user.company)
        trainings = Building.objects.filter(airport_id__in=airports)

        return trainings


class BuildingsDetailView(LoginRequiredMixin, DetailView):
    model = Building
    template_name = "airport_facilities/buildings_details.html"


class BuildingsCreateView(LoginRequiredMixin, CreateView):
    model = Building
    template_name = "airport_facilities/buildings_form.html"

    form_class = CreateBuilding

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company)
        form.instance.airport = airports
        return super().form_valid(form)


class BuildingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Building
    template_name = "airport_facilities/buildings_form.html"

    form_class = CreateBuilding


class BuildingsDeleteView(DeleteView):
    model = Building
    template_name = "airport_facilities/buildings_delete.html"
    success_url = reverse_lazy("buildings")


def other_facilities(request):
    user = request.user
    airports = Airport.objects.filter(company_id=user.company)
    return render(
        request,
        "airport_facilities/other_facilities.html",
        {
            "vehicles": Vehicle.objects.filter(airport__in=airports),
            "properties": Property.objects.filter(airport__in=airports),
            "others": Others.objects.filter(airport__in=airports),
        },
    )


class VehiclesDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_details.html"


class VehiclesCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_form.html"

    form_class = CreateVehicle

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company)
        if airports.exists():
            form.instance.airport = airports.first()
        return super().form_valid(form)


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

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company)
        if airports.exists():
            form.instance.airport = airports.first()
        return super().form_valid(form)


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

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company)
        if airports.exists():
            form.instance.airport = airports.first()
        return super().form_valid(form)


class OthersUpdateView(LoginRequiredMixin, UpdateView):
    model = Others
    template_name = "airport_facilities/others_form.html"

    form_class = CreateOthers


class OthersDeleteView(DeleteView):
    model = Others
    template_name = "airport_facilities/others_delete.html"
    success_url = reverse_lazy("other_facilities")
