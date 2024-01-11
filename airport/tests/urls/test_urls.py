from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import (
    AirportFactory,
    RunwayFactory,
    OutsideAircraftStandFactory,
    HangarFactory,
)


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create()
        self.runway = RunwayFactory.create()
        self.outside_stand = OutsideAircraftStandFactory.create()
        self.hangar = HangarFactory.create()

    def test_airport_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse(
            "airports",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_airport_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("airports_update", kwargs={"pk": self.airport.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_runways_and_runways_add_url_returns_200_status_code_for_standard_get(self):
        urls = ["runways", "runways_add"]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_runways_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("runways_details", kwargs={"pk": self.runway.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_runways_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("runways_update", kwargs={"pk": self.runway.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_runways_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("runways_delete", kwargs={"pk": self.runway.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_airport_stands_and_hangars_url_test_runways_delete_url_returns_200_status_code_for_standard_get(
        self,
    ):
        urls = ["aircraft_stands", "hangars_add", "outside_stands_add"]

        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)

                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_hangars_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_hangars_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("hangars_delete", kwargs={"pk": self.hangar.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_hangars_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("hangars_update", kwargs={"pk": self.hangar.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_outside_stands_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("outside_stands_details", kwargs={"pk": self.outside_stand.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_outside_stands_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("outside_stands_update", kwargs={"pk": self.outside_stand.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_outside_stands_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("outside_stands_delete", kwargs={"pk": self.outside_stand.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
