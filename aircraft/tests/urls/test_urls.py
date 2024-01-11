from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from django.contrib.auth.models import Group
from aircraft.factories import AircraftFactory, AircraftHangaredFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create()
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
        )

    def test_aircraft_url_returns_200_status_code_for_standard_get(self):
        urls = ["aircrafts", "aircrafts_add"]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_aircrafts_details_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aircrafts_update_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("aircrafts_update", kwargs={"pk": self.aircraft.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aircrafts_delete_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("aircrafts_delete", kwargs={"pk": self.aircraft.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aircraft_hangared_add_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("aircrafts_hangared_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aircraft_hangared_details_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse(
            "aircrafts_hangared_details", kwargs={"pk": self.aircraft_hanagared.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aircraft_hangared_delete_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse(
            "aircrafts_hangared_delete", kwargs={"pk": self.aircraft_hanagared.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_aircraft_hangared_update_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse(
            "aircrafts_hangared_update", kwargs={"pk": self.aircraft_hanagared.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
