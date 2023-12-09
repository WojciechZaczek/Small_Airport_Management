from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from airport.models import Airport, Runway
from notifications.models import Notification
from django.views.generic import TemplateView
from datetime import datetime
import requests
import os
from django.conf import settings
from typing import Dict, Any


class APIWeather:
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_data(self, city_name: str) -> requests.Response:
        return requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.WEATHER_KEY}&units=metric"
        )

    def build_url(self, city_name: str) -> str:
        return f"{APIWeather.API_URL}?q={city_name}&appid={settings.WEATHER_KEY}&units=metric"

    def parse_data(self, response) -> Dict[str, Any]:
        temperature = response.get("main", {}).get("temp")
        humidity = response.get("main", {}).get("humidity")
        wind = response.get("wind", {}).get("speed")
        clouds = response.get("clouds", {}).get("all")
        weather_description = response.get("weather", [{}])[0].get("main")
        weather_icon_code = response.get("weather", [{}])[0].get("icon")
        weather_icon_url = (
            f"https://openweathermap.org/img/wn/{weather_icon_code}@2x.png"
        )
        last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "weather_temperature": temperature,
            "weather_humidity": humidity,
            "weather_wind": wind,
            "weather_clouds": clouds,
            "weather_description": weather_description,
            "weather_icon": weather_icon_url,
            "last_update": last_update,
        }

    def get_weather_data(self, user):
        city_name = Airport.objects.filter(company=user.company).first().city
        response = self.fetch_data(city_name).json()
        data = self.parse_data(response)
        return data


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_weather_client = APIWeather()
        context.update(api_weather_client.get_weather_data(user=self.request.user))
        context.update(self.get_airport_data())
        return context

    def get_airport_data(self):
        todays_notification = Notification.objects.filter(
            view_date=timezone.localdate()
        )
        users_airport = Airport.objects.filter(company=self.request.user.company)
        airport = users_airport.values_list("id", flat=True)
        runways = Runway.objects.filter(airport__in=airport)

        return {
            "title": "Home",
            "airports": users_airport,
            "runways": runways,
            "notifications": todays_notification,
        }

    # def get_weather_data(self):
    #
    #     city_name = Airport.objects.filter(company=self.request.user.company).first().city
    #     response = requests.get(
    #         f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.WEATHER_KEY}&units=metric"
    #     ).json()
    #     temperature = response.get("main", {}).get("temp")
    #     humidity = response.get("main", {}).get("humidity")
    #     wind = response.get("wind", {}).get("speed")
    #     clouds = response.get("clouds", {}).get("all")
    #     weather_description = response.get("weather", [{}])[0].get("main")
    #     weather_icon_code = response.get("weather", [{}])[0].get("icon")
    #     weather_icon_url = f"https://openweathermap.org/img/wn/{weather_icon_code}@2x.png"
    #     last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #
    #     return {
    #         "weather_temperature": temperature,
    #         "weather_humidity": humidity,
    #         "weather_wind": wind,
    #         "weather_clouds": clouds,
    #         "weather_description": weather_description,
    #         "weather_icon": weather_icon_url,
    #         "last_update": last_update
    #     }


# def home(request):
#
#     # method
#     todays_notification = Notification.objects.filter(view_date=timezone.localdate())
#     users_airport = Airport.objects.filter(company=request.user.company)
#
#     airport = users_airport.values_list("id", flat=True)
#
#     runways = Runway.objects.filter(airport__in=airport)
#     city_name = users_airport.first().city
#
#     # method
#     response = requests.get(
#         f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.WEATHER_KEY}&units=metric"
#     ).json()
#     temperature = response.get("main", {}).get("temp")
#     humidity = response.get("main", {}).get("humidity")
#     wind = response.get("wind", {}).get("speed")
#     clouds = response.get("clouds", {}).get("all")
#     weather_description = response.get("weather", [{}])[0].get("main")
#     weather_icon_code = response.get("weather", [{}])[0].get("icon")
#     weather_icon_url = f"https://openweathermap.org/img/wn/{weather_icon_code}@2x.png"
#     last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # method
#     return render(
#         request,
#         "dashboard/dashboard.html",
#         {
#             "title": "Home",
#             "airports": users_airport,
#             "runways": runways,
#             "notifications": todays_notification,
#             "weather_temperature": temperature,
#             "weather_humidity": humidity,
#             "weather_wind": wind,
#             "weather_clouds": clouds,
#             "weather_description": weather_description,
#             "weather_icon": weather_icon_url,
#             "last_update": last_update
#
#         },
#     )
