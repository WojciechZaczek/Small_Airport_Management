from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from aircraft.models import AircraftHangared
from .models import Runway, Airport, Hangar, OutsideAircraftStand
from .forms import CreatRunway, CreatAirport, CreatHangar, CreatOutsideStand


class AirportListView(LoginRequiredMixin, ListView):
    model = Airport
    template_name = "airport/airport.html"
    context_object_name = "airport"

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        return airports


class AirportUpdateView(LoginRequiredMixin, UpdateView):
    model = Airport
    template_name = "airport/airport_form.html"
    form_class = CreatAirport

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class AirportCreateView(LoginRequiredMixin, CreateView):
    model = Airport
    template_name = "airport/airport_form.html"
    form_class = CreatAirport

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class AirportDeleteView(LoginRequiredMixin, DeleteView):
    model = Airport
    template_name = "airport/airport_delete.html"
    success_url = reverse_lazy("airports")


class RunwaysListView(LoginRequiredMixin, ListView):
    model = Runway
    template_name = "airport/runways.html"
    context_object_name = "runways"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_company = self.request.user.company
        context["airports"] = Airport.objects.filter(company=user_company)
        return context

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        runways = Runway.objects.filter(airport__in=airports)

        return runways


class RunwaysDetailView(LoginRequiredMixin, DetailView):
    model = Runway
    template_name = "airport/runways_details.html"


class RunwaysCreateView(LoginRequiredMixin, CreateView):
    model = Runway
    template_name = "airport/runways_form.html"

    form_class = CreatRunway

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class RunwaysUpdateView(LoginRequiredMixin, UpdateView):
    model = Runway
    template_name = "airport/runways_form.html"
    form_class = CreatRunway

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class RunwaysDeleteView(LoginRequiredMixin, DeleteView):
    model = Runway
    template_name = "airport/runways_delete.html"
    success_url = reverse_lazy("runways")


@login_required()
def aircraft_stands(request):
    user = request.user
    airports = Airport.objects.filter(company=user.company)
    return render(
        request,
        "airport/aircraft_stands.html",
        {
            "title": "Aircraft stands",
            "hangars": Hangar.objects.filter(airport__in=airports),
            "outside_stands": OutsideAircraftStand.objects.filter(airport__in=airports),
            "airports": airports,
        },
    )


class HangarsDetailView(LoginRequiredMixin, DetailView):
    model = Hangar

    template_name = "airport/hangars_details.html"
    extra_context = {"aircrafts": AircraftHangared.objects.all()}


class HangarsCreateView(LoginRequiredMixin, CreateView):
    model = Hangar
    template_name = "airport/hangars_form.html"
    form_class = CreatHangar

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class HangarsUpdateView(LoginRequiredMixin, UpdateView):
    model = Hangar
    template_name = "airport/hangars_form.html"

    form_class = CreatHangar

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class HangarsDeleteView(LoginRequiredMixin, DeleteView):
    model = Hangar
    template_name = "airport/hangars_delete.html"
    success_url = reverse_lazy("aircraft_stands")


class OutsideStandsDetailView(LoginRequiredMixin, DetailView):
    model = OutsideAircraftStand

    template_name = "airport/outside_stands_details.html"
    extra_context = {"aircrafts": AircraftHangared.objects.all()}


class OutsideStandsCreateView(LoginRequiredMixin, CreateView):
    model = OutsideAircraftStand
    template_name = "airport/outside_stands_form.html"
    form_class = CreatOutsideStand

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class OutsideStandsUpdateView(LoginRequiredMixin, UpdateView):
    model = OutsideAircraftStand
    template_name = "airport/outside_stands_form.html"

    form_class = CreatOutsideStand

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class OutsideStandsDeleteView(LoginRequiredMixin, DeleteView):
    model = OutsideAircraftStand
    template_name = "airport/outside_stands_delete.html"
    success_url = reverse_lazy("aircraft_stands")
