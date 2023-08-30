from django.shortcuts import render
from .models import Building, Others, Property, Vehicle


def buildings(request):
    return render(request, "airport_facilities/buildings.html", {"title": "Buildings"})


def other_facilities(request):
    return render(
        request,
        "airport_facilities/other_facilities.html",
        {"title": "Other facilities"},
    )
