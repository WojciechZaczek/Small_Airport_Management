from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Offer, Training
from .forms import CreateTraining
from airport.models import Airport


class TrainingsListView(LoginRequiredMixin, ListView):
    model = Training
    template_name = "offer/trainings.html"
    context_object_name = "trainings"

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company_id)
        trainings = Training.objects.filter(airport_id__in=airports)

        return trainings


class TrainingsDetailView(LoginRequiredMixin, DetailView):
    model = Training
    template_name = "offer/trainings_details.html"


class TrainingsCreateView(LoginRequiredMixin, CreateView):
    model = Training
    template_name = "offer/trainings_form.html"

    form_class = CreateTraining


class TrainingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Training
    template_name = "offer/trainings_form.html"

    form_class = CreateTraining


class TrainingsDeleteView(DeleteView):
    model = Training
    template_name = "offer/trainings_delete.html"
    success_url = reverse_lazy("trainings")


class OffersListView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = "offer/trainings.html"
    context_object_name = "trainings"

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company_id=user.company_id)
        offers = Offer.objects.filter(airport_id__in=airports)

        return offers


class OffersDetailView(LoginRequiredMixin, DetailView):
    model = Offer
    template_name = "offer/offers_details.html"


class OffersCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    template_name = "offer/offers_form.html"

    form_class = CreateTraining


class OffersUpdateView(LoginRequiredMixin, UpdateView):
    model = Offer
    template_name = "offer/offers_form.html"

    form_class = CreateTraining


class OffersDeleteView(DeleteView):
    model = Offer
    template_name = "offer/offers_delete.html"
    success_url = reverse_lazy("offers")
