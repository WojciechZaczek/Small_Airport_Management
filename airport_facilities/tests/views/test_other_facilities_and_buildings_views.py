from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import (
    BuildingFactory,
    VehicleFactory,
    OthersFactory,
    PropertyFactory,
)
from organization.factories import DepartmentFactory
from airport_facilities.models import Building


class OtherFacilitiesViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)

        self.vehicle = VehicleFactory.create(
            airport=self.airport, registration_no="test1234"
        )
        self.property = PropertyFactory.create(
            airport=self.airport, name="Property one"
        )
        self.others = OthersFactory.create(airport=self.airport, name="Others one")

    def test_view_other_facilities_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertTemplateUsed(response, "airport_facilities/other_facilities.html")

    def test_view_other_facilities_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/other-facilities/")

    def test_view_other_facilities_returns_correct_vehicle_registration_no_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "test1234")

    def test_view_other_facilities_returns_correct_vehicle_department_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.vehicle.department.name)

    def test_view_other_facilities_returns_correct_property_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Property one")

    def test_view_other_facilities_returns_correct_property_department_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.property.department.name)

    def test_view_other_facilities_returns_correct_others_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Others one")

    def test_view_other_facilities_returns_correct_others_department_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.others.department.name)


class BuildingsListViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.building = BuildingFactory.create(
            airport=self.airport, name="Building one"
        )

    def test_view_buildings_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("buildings"))
        self.assertTemplateUsed(response, "airport_facilities/buildings.html")

    def test_view_buildings_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("buildings"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/buildings/")

    def test_view_buildings_returns_correct_building_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("buildings"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Building one")

    def test_buildings_view_displayed_department_length_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("buildings"))
        self.assertContains(response, self.building.department)


class BuildingsDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.building = BuildingFactory.create(airport=self.airport)

    def test_view_buildings_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("buildings_details", kwargs={"pk": self.building.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/buildings_details.html")

    def test_view_buildings_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("buildings_details", kwargs={"pk": self.building.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/buildings/{self.building.pk}/")

    def test_buildings_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("buildings_details", kwargs={"pk": self.building.pk})
        )
        self.assertContains(response, self.building.name)


class BuildingsCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory(company=self.user.company)
        self.new_building_data = {
            "name": "Alfa Building",
            "description": "test description",
            "department": self.department.pk,
            "airport": self.airport.pk,
        }

    def test_view_buildings_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("buildings_add"))
        self.assertTemplateUsed(response, "airport_facilities/buildings_form.html")

    def test_view_buildings_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("buildings_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/buildings/new/")

    def test_view_buildings_create_creates_new_building_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Building.objects.count(), 0)
        response = self.client.post(reverse("buildings_add"), self.new_building_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Building.objects.count(), 1)

    def test_view_buildings_create_creates_new_building_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(reverse("buildings_add"), self.new_building_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_building = Building.objects.first()
        self.assertEqual(new_building.name, "Alfa Building")


class BuildingsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.user.company)
        self.building = BuildingFactory.create(airport=self.airport)

    def test_view_buildings_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("buildings_update", kwargs={"pk": self.building.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/buildings_form.html")

    def test_view_buildings_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("buildings_update", kwargs={"pk": self.building.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/buildings/{self.building.pk}/update/"
        )

    def test_view_buildings_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Alfa Building",
            "description": self.building.description,
            "department": self.department.pk,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("buildings_update", kwargs={"pk": self.building.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.building.refresh_from_db()
        self.assertEqual(self.building.name, update["name"])


class BuildingsDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.building = BuildingFactory.create(airport=self.airport)

    def test_view_buildings_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("buildings_delete", kwargs={"pk": self.building.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/buildings_delete.html")

    def test_view_buildings_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("buildings_delete", kwargs={"pk": self.building.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/buildings/{self.building.pk}/delete/"
        )

    def test_buildings_delete_view_deletes_building_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Building.objects.count(), 1)
        response = self.client.delete(
            reverse("buildings_delete", kwargs={"pk": self.building.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Building.objects.count(), 0)
