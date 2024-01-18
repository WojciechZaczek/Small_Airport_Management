from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import (
    BuildingFactory,
    VehicleFactory,
    OthersFactory,
    PropertyFactory,
)


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/other-facilities/")

    def test_view_other_facilities_returns_correct_vehicle_registration_no_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test1234")

    def test_view_other_facilities_returns_correct_vehicle_department_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.vehicle.department.name)

    def test_view_other_facilities_returns_correct_property_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Property one")

    def test_view_other_facilities_returns_correct_property_department_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.property.department.name)

    def test_view_other_facilities_returns_correct_others_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Others one")

    def test_view_other_facilities_returns_correct_others_department_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("other_facilities"))
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/buildings/")

    def test_view_buildings_returns_correct_building_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("buildings"))
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/buildings/1/")

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
        self.building = BuildingFactory.create(airport=self.airport)

    def test_view_buildings_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("buildings_add"))
        self.assertTemplateUsed(response, "airport_facilities/buildings_form.html")

    def test_view_buildings_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("buildings_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/buildings/new/")


class BuildingsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/buildings/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/buildings/1/delete/")
