from django.shortcuts import render
from .models import Offer, Training


def offer(request):
    return render(request, "offer/offer.html", {"title": "Offer"})


def trainings(request):
    return render(request, "offer/trainings.html", {"title": "Trainings"})
