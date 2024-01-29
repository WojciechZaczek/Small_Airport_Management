from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Building, Others, Property, Vehicle
from .forms import CreateBuilding, CreateVehicle, CreateProperty, CreateOthers
from airport.models import Airport


class BuildingsListView(LoginRequiredMixin, ListView):
    model = Building
    template_name = "airport_facilities/buildings.html"
    context_object_name = "buildings"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user_company = self.request.user.company
        context["airports"] = Airport.objects.filter(company=user_company)
        return context

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        buildings = Building.objects.filter(airport__in=airports)

        return buildings


class BuildingsDetailView(LoginRequiredMixin, DetailView):
    model = Building
    template_name = "airport_facilities/buildings_details.html"


class BuildingsCreateView(LoginRequiredMixin, CreateView):
    model = Building
    template_name = "airport_facilities/buildings_form.html"
    form_class = CreateBuilding

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class BuildingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Building
    template_name = "airport_facilities/buildings_form.html"

    form_class = CreateBuilding

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class BuildingsDeleteView(LoginRequiredMixin, DeleteView):
    model = Building
    template_name = "airport_facilities/buildings_delete.html"
    success_url = reverse_lazy("buildings")


@login_required()
def other_facilities(request):
    user = request.user
    airports = Airport.objects.filter(company=user.company)
    return render(
        request,
        "airport_facilities/other_facilities.html",
        {
            "airports": airports,
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class VehiclesUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = "airport_facilities/vehicles_form.html"
    form_class = CreateVehicle

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class VehiclesDeleteView(LoginRequiredMixin, DeleteView):
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class PropertiesUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    template_name = "airport_facilities/properties_form.html"

    form_class = CreateProperty

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class PropertiesDeleteView(LoginRequiredMixin, DeleteView):
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class OthersUpdateView(LoginRequiredMixin, UpdateView):
    model = Others
    template_name = "airport_facilities/others_form.html"
    form_class = CreateOthers

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class OthersDeleteView(LoginRequiredMixin, DeleteView):
    model = Others
    template_name = "airport_facilities/others_delete.html"
    success_url = reverse_lazy("other_facilities")
