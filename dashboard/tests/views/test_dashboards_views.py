from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from unittest.mock import patch
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import AirportFactory, RunwayFactory
from notifications.factories import NotificationFactory
from dashboard.views import APIWeather


class DashboardViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company, city="London")
        self.runway = RunwayFactory.create(airport=self.airport)
        self.notification = NotificationFactory.create(
            airport=self.airport, view_date=timezone.now()
        )

    def test_view_dashboard_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

    def test_view_dashboard_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/home/")

    @patch.object(APIWeather, "fetch_data")
    def test_view_dashboard_get_weather_data(self, mock_fetch_data):
        mock_response = {
            "main": {"temp": 20, "humidity": 50},
            "wind": {"speed": 10},
            "clouds": {"all": 20},
            "weather": [{"main": "Clear", "icon": "01d"}],
        }

        mock_fetch_data.return_value.json.return_value = mock_response
        api_weather_client = APIWeather()
        weather_data = api_weather_client.get_weather_data(city_name="Test city")
        self.assertEqual(weather_data["weather_temperature"], 20)
        self.assertEqual(weather_data["weather_humidity"], 50)
        self.assertEqual(weather_data["weather_wind"], 10)
        self.assertEqual(weather_data["weather_clouds"], 20)
        self.assertEqual(weather_data["weather_description"], "Clear")
