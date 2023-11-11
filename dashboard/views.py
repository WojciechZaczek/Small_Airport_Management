from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from airport.models import Airport, Runway
from notifications.models import Notification
import requests


@login_required()
def home(request):
    todays_notification = Notification.objects.filter(view_date=timezone.localdate())
    users_airport = Airport.objects.filter(company=request.user.company)

    airport = users_airport.values_list("id", flat=True)

    runways = Runway.objects.filter(airport__in=airport)

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Gdańsk&appid=0d18d8cccd158b10da75c1fbfa3e3fba&units=metric"
    ).json()

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "title": "Home",
            "airports": users_airport,
            "runways": runways,
            "notifications": todays_notification,
            "weather": response,
        },
    )
