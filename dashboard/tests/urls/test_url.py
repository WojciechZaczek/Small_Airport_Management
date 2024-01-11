from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import AirportFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)

    def test_dashboard_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
