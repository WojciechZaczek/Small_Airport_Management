from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from airport.models import Airport, Runway
from .models import AircraftHangared, Aircraft
from .forms import CreatAircraft, CreatAircraftHangared
from django.contrib.auth.mixins import PermissionRequiredMixin


@login_required()
def aircraft(request):
    aircrafts = Aircraft.objects.all()
    user = request.user
    airports = Airport.objects.filter(company=user.company)
    runways = Runway.objects.filter(airport__in=airports)

    for aircraft in aircrafts:
        aircraft.can_land = aircraft.can_land_at_airport(runways)

    return render(
        request,
        "aircraft/aircrafts.html",
        {
            "title": "Aircrafts",
            "aircrafts": aircrafts,
            "aircrafts_hangared": AircraftHangared.objects.filter(airport__in=airports),
        },
    )


class AircraftsDetailView(LoginRequiredMixin, DetailView):
    model = Aircraft
    template_name = "aircraft/aircrafts_details.html"


class AircraftsUpdateView(LoginRequiredMixin, UpdateView):
    model = Aircraft
    template_name = "aircraft/aircrafts_form.html"
    form_class = CreatAircraft


class AircraftsCreateView(LoginRequiredMixin, CreateView):
    model = Aircraft
    template_name = "aircraft/aircrafts_form.html"

    form_class = CreatAircraft


class AircraftsDeleteView(LoginRequiredMixin, DeleteView):
    model = Aircraft
    template_name = "aircraft/aircraft_delete.html"
    success_url = reverse_lazy("aircrafts")


class AircraftsHangaredDetailView(LoginRequiredMixin, DetailView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_details.html"


class AircraftsHangaredUpdateView(LoginRequiredMixin, UpdateView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_form.html"

    form_class = CreatAircraftHangared

    def get_form(self, form_class=None):
        return super().get_form(form_class)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class AircraftsHangaredCreateView(LoginRequiredMixin, CreateView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_form.html"

    form_class = CreatAircraftHangared

    def form_valid(self, form):
        user = self.request.user
        user_company = user.company
        try:
            airport = Airport.objects.get(company=user_company)
        except Airport.DoesNotExist:
            pass
        else:
            form.instance.airport = airport
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class AircraftsHangaredDeleteView(LoginRequiredMixin, DeleteView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_delete.html"
    success_url = reverse_lazy("aircrafts")
