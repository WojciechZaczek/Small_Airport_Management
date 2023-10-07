from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required

from airport.models import Airport, Hangar, OutsideAircraftStand, Runway
from .models import AircraftHangared, Aircraft
from .forms import CreatAircraft, CreatAircraftHangared
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def aircraft(request):
    aircrafts = Aircraft.objects.all()

    user = request.user
    airports = Airport.objects.filter(company_id=user.company_id)
    runways = Runway.objects.filter(airport_id__in=airports)

    for aircraft in aircrafts:
        aircraft.can_land = aircraft.can_land_at_airport(runways)

    return render(
        request,
        "aircraft/aircrafts.html",
        {
            "title": "Aircrafts",
            "aircrafts": aircrafts,
            "aircrafts_hangared": AircraftHangared.objects.filter(
                airport_id__in=airports
            ),
        },
    )


class AircraftsDetailView(DetailView):
    model = Aircraft
    template_name = "aircraft/aircrafts_details.html"


class AircraftsUpdateView(UpdateView):
    model = Aircraft
    template_name = "aircraft/aircrafts_form.html"

    form_class = CreatAircraft


class AircraftsCreateView(CreateView):
    model = Aircraft
    template_name = "aircraft/aircrafts_form.html"

    form_class = CreatAircraft


class AircraftsDeleteView(DeleteView):
    model = Aircraft
    template_name = "aircraft/aircraft_delete.html"
    success_url = reverse_lazy("aircrafts")


class AircraftsHangaredDetailView(DetailView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_details.html"


class AircraftsHangaredUpdateView(UpdateView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_form.html"

    form_class = CreatAircraftHangared


class AircraftsHangaredCreateView(LoginRequiredMixin, CreateView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_form.html"

    form_class = CreatAircraftHangared

    def form_valid(self, form):
        user = self.request.user
        user_company = user.company_id
        try:
            airport = Airport.objects.get(company_id=user_company)
        except Airport.DoesNotExist:
            pass
        else:
            form.instance.airport_id = airport
        return super().form_valid(form)


class AircraftsHangaredDeleteView(DeleteView):
    model = AircraftHangared
    template_name = "aircraft/aircrafts_hangared_delete.html"
    success_url = reverse_lazy("aircrafts")
