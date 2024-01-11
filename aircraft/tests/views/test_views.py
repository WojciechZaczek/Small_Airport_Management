from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from aircraft.factories import AircraftFactory, AircraftHangaredFactory


class AircraftView(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create(username="testuser", password="testpassword")
        self.aircraft = AircraftFactory.create(manufacture="Boeing")
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
        )

    def test_view_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        self.assertTemplateUsed(response, "aircraft/aircrafts.html")

    def test_view_returns_correct_aircraft_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        self.assertContains(response, "Boeing")
