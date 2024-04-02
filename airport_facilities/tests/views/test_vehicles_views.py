from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from http import HTTPStatus
from airport.factories import AirportFactory
from airport_facilities.factories import VehicleFactory
from airport_facilities.models import Vehicle
from organization.factories import DepartmentFactory


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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/vehicles/{self.vehicle.pk}/")

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
        self.department = DepartmentFactory(company=self.user.company)
        self.new_vehicle_data = {
            "type": "Test Car",
            "registration_no": "RR1111",
            "description": "test description",
            "department": self.department.pk,
            "airport": self.airport.pk,
        }

    def test_view_vehicles_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("vehicles_add"))
        self.assertTemplateUsed(response, "airport_facilities/vehicles_form.html")

    def test_view_vehicles_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("vehicles_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/vehicles/new/")

    def test_view_vehicles_create_creates_new_vehicle_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Vehicle.objects.count(), 0)
        response = self.client.post(reverse("vehicles_add"), self.new_vehicle_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Vehicle.objects.count(), 1)

    def test_view_vehicles_create_creates_new_vehicle_object_with_correct_content(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("vehicles_add"), self.new_vehicle_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_vehicle = Vehicle.objects.first()
        self.assertEqual(new_vehicle.type, "Test Car")


class VehicleUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.user.company)
        self.vehicle = VehicleFactory.create(airport=self.airport)

    def test_view_vehicles_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("vehicles_update", kwargs={"pk": self.vehicle.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/vehicles_form.html")

    def test_view_vehicle_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("vehicles_update", kwargs={"pk": self.vehicle.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/vehicles/{self.vehicle.pk}/update/"
        )

    def test_view_vehicle_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "type": "Test Car",
            "registration_no": self.vehicle.registration_no,
            "description": self.vehicle.description,
            "department": self.department.pk,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("vehicles_update", kwargs={"pk": self.vehicle.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.type, update["type"])


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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/vehicles/{self.vehicle.pk}/delete/"
        )

    def test_vehicles_delete_view_deletes_vehicle_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Vehicle.objects.count(), 1)
        response = self.client.delete(
            reverse("vehicles_delete", kwargs={"pk": self.vehicle.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Vehicle.objects.count(), 0)
