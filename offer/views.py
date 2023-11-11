from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from airport.models import Airport
from .forms import CreateTraining, CreateOffer
from .models import Offer, Training


class TrainingsListView(LoginRequiredMixin, ListView):
    model = Training
    template_name = "offer/trainings.html"
    context_object_name = "trainings"

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        trainings = Training.objects.filter(airport__in=airports)

        return trainings


class TrainingsDetailView(LoginRequiredMixin, DetailView):
    model = Training
    template_name = "offer/trainings_details.html"


class TrainingsCreateView(LoginRequiredMixin, CreateView):
    model = Training
    template_name = "offer/trainings_form.html"

    form_class = CreateTraining

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        if airports.exists():
            form.instance.airport = airports.first()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TrainingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Training
    template_name = "offer/trainings_form.html"

    form_class = CreateTraining

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TrainingsDeleteView(LoginRequiredMixin, DeleteView):
    model = Training
    template_name = "offer/trainings_delete.html"
    success_url = reverse_lazy("trainings")


class OffersListView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = "offer/offers.html"
    context_object_name = "offers"

    def get_queryset(self):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        offers = Offer.objects.filter(airport__in=airports)

        return offers


class OffersDetailView(LoginRequiredMixin, DetailView):
    model = Offer
    template_name = "offer/offers_details.html"


class OffersCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    template_name = "offer/offers_form.html"

    form_class = CreateOffer

    def form_valid(self, form):
        user = self.request.user
        airports = Airport.objects.filter(company=user.company)
        if airports.exists():
            form.instance.airport = airports.first()
        return super().form_valid(form)


class OffersUpdateView(LoginRequiredMixin, UpdateView):
    model = Offer
    template_name = "offer/offers_form.html"

    form_class = CreateOffer


class OffersDeleteView(LoginRequiredMixin, DeleteView):
    model = Offer
    template_name = "offer/offers_delete.html"
    success_url = reverse_lazy("offers")
