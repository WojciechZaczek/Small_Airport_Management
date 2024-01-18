from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import VehicleFactory


class VehicleDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.vehicle = VehicleFactory.create(airport=self.airport)

    def test_view_vehicles_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("vehicles_details", kwargs={"pk": self.vehicle.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/vehicles_details.html")

    def test_view_others_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("vehicles_details", kwargs={"pk": self.vehicle.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/vehicles/1/")

    def test_vehicles_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("vehicles_details", kwargs={"pk": self.vehicle.pk})
        )
        self.assertContains(response, self.vehicle.registration_no)


class VehicleCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.vehicle = VehicleFactory.create(airport=self.airport)

    def test_view_vehicles_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("vehicles_add"))
        self.assertTemplateUsed(response, "airport_facilities/vehicles_form.html")

    def test_view_vehicles_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("vehicles_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/vehicles/new/")


class VehicleUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.vehicle = VehicleFactory.create(airport=self.airport)

    def test_view_vehicles_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("vehicles_update", kwargs={"pk": self.vehicle.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/vehicles_form.html")

    def test_view_vehicle_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("others_update", kwargs={"pk": self.vehicle.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/others/1/update/")


class VehicleDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.vehicle = VehicleFactory.create(airport=self.airport)

    def test_view_vehicles_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("vehicles_delete", kwargs={"pk": self.vehicle.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/vehicles_delete.html")

    def test_view_vehicles_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("vehicles_delete", kwargs={"pk": self.vehicle.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/vehicles/1/delete/")
