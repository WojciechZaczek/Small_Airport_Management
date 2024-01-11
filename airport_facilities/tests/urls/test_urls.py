from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport_facilities.factories import (
    BuildingFactory,
    VehicleFactory,
    PropertyFactory,
    OthersFactory,
)


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.building = BuildingFactory.create()
        self.vehicle = VehicleFactory.create()
        self.property = PropertyFactory.create()
        self.other = OthersFactory.create()

    def test_buildings_url_returns_200_status_code_for_standard_get(self):
        urls = ["buildings", "buildings_add", "other_facilities"]

        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_buildings_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("buildings_details", kwargs={"pk": self.building.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_buildings_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("buildings_update", kwargs={"pk": self.building.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_buildings_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("buildings_delete", kwargs={"pk": self.building.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicles_add_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("vehicles_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicles_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("vehicles_details", kwargs={"pk": self.vehicle.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicles_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("vehicles_update", kwargs={"pk": self.vehicle.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicles_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("vehicles_delete", kwargs={"pk": self.vehicle.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_properties_add_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("properties_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_properties_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("properties_details", kwargs={"pk": self.property.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_properties_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("properties_update", kwargs={"pk": self.property.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_properties_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("properties_delete", kwargs={"pk": self.property.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_others_add_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("others_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_others_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("others_details", kwargs={"pk": self.other.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_others_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("others_update", kwargs={"pk": self.other.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_others_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("others_delete", kwargs={"pk": self.other.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
