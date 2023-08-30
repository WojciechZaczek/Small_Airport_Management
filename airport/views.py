from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Runway, Airport
from .forms import CreatRunway, CreatAirport


class AirportListView(ListView):
    model = Airport
    template_name = "airport/airport.html"
    context_object_name = "airport"


class AirportUpdateView(UpdateView):
    model = Airport
    template_name = "airport/airport_form.html"

    form_class = CreatAirport


class RunwaysListView(ListView):
    model = Runway
    template_name = "airport/runways.html"
    context_object_name = "runways"


class RunwaysDetailView(DetailView):
    model = Runway
    template_name = "airport/runways_detail.html"


class RunwaysCreateView(CreateView):
    model = Runway
    template_name = "airport/runways_form.html"

    form_class = CreatRunway


class RunwaysUpdateView(UpdateView):
    model = Runway
    template_name = "airport/runways_form.html"

    form_class = CreatRunway


class RunwaysDeleteView(DeleteView):
    model = Runway
    template_name = "airport/runways_delete.html"
    success_url = reverse_lazy("runways")
