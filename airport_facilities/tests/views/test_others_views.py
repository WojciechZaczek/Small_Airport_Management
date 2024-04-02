from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import OthersFactory
from airport_facilities.models import Others
from organization.factories import DepartmentFactory


class OthersDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.other = OthersFactory.create(airport=self.airport)

    def test_view_others_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("others_details", kwargs={"pk": self.other.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/others_details.html")

    def test_view_others_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("others_details", kwargs={"pk": self.other.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/others/{self.other.pk}/")

    def test_others_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("others_details", kwargs={"pk": self.other.pk})
        )
        self.assertContains(response, self.other.name)


class OthersCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory(company=self.user.company)
        self.new_other_data = {
            "name": "Alfa Other",
            "description": "test description",
            "department": self.department.pk,
            "airport": self.airport.pk,
        }

    def test_view_others_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("others_add"))
        self.assertTemplateUsed(response, "airport_facilities/others_form.html")

    def test_view_others_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("others_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/others/new/")

    def test_view_others_create_creates_new_other_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Others.objects.count(), 0)
        response = self.client.post(reverse("others_add"), self.new_other_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Others.objects.count(), 1)

    def test_view_others_create_creates_new_other_object_with_correct_content(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("others_add"), self.new_other_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_other = Others.objects.first()
        self.assertEqual(new_other.name, "Alfa Other")


class OthersUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.department = DepartmentFactory.create(company=self.user.company)
        self.other = OthersFactory.create(airport=self.airport)

    def test_view_others_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("others_update", kwargs={"pk": self.other.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/others_form.html")

    def test_view_others_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("others_update", kwargs={"pk": self.other.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/others/{self.other.pk}/update/")

    def test_view_others_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Test Other",
            "description": self.other.description,
            "department": self.department.pk,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("others_update", kwargs={"pk": self.other.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.other.refresh_from_db()
        self.assertEqual(self.other.name, update["name"])


class OthersDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.other = OthersFactory.create(airport=self.airport)

    def test_view_others_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("others_delete", kwargs={"pk": self.other.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/others_delete.html")

    def test_view_others_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("others_delete", kwargs={"pk": self.other.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/others/{self.other.pk}/delete/")

    def test_others_delete_view_deletes_others_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Others.objects.count(), 1)
        response = self.client.delete(
            reverse("others_delete", kwargs={"pk": self.other.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Others.objects.count(), 0)
