from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import PropertyFactory
from airport_facilities.models import Property
from organization.factories import DepartmentFactory


class PropertiesDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)

    def testproperties_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_details", kwargs={"pk": self.property.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/properties_details.html")

    def test_view_properties_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("properties_details", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/properties/1/")

    def test_properties_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_details", kwargs={"pk": self.property.pk})
        )
        self.assertContains(response, self.property.name)


class PropertiesCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory(company=self.user.company)
        self.new_property_data = {
            "name": "Test Property",
            "description": "test description",
            "department": self.department.pk,
            "airport": self.airport.pk,
        }

    def test_view_properties_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("properties_add"))
        self.assertTemplateUsed(response, "airport_facilities/properties_form.html")

    def test_view_properties_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("properties_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/properties/new/")

    def test_view_properties_create_creates_new_property_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Property.objects.count(), 0)
        response = self.client.post(reverse("properties_add"), self.new_property_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Property.objects.count(), 1)

    def test_view_properties_create_creates_new_property_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(reverse("properties_add"), self.new_property_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_property = Property.objects.first()
        self.assertEqual(new_property.name, "Test Property")


class PropertiesUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)
        self.department = DepartmentFactory.create(company=self.user.company)

    def test_view_properties_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_update", kwargs={"pk": self.property.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/properties_form.html")

    def test_view_properties_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("properties_update", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/properties/1/update/")

    def test_view_properties_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Alfa Property",
            "description": self.property.description,
            "department": self.department.pk,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("properties_update", kwargs={"pk": self.property.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.property.refresh_from_db()
        self.assertEqual(self.property.name, update["name"])


class PropertiesDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)

    def test_view_properties_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_delete", kwargs={"pk": self.property.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/properties_delete.html")

    def test_view_properties_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("properties_delete", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/properties/1/delete/")

    def test_properties_delete_view_deletes_property_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Property.objects.count(), 1)
        response = self.client.delete(
            reverse("properties_delete", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Property.objects.count(), 0)
