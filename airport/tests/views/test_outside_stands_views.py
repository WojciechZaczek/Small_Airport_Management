from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import (
    AirportFactory,
    RunwayFactory,
    HangarFactory,
    OutsideAircraftStandFactory,
)
from airport.models import OutsideAircraftStand


class OutsideAircraftStandDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)

        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_outside_details_stands_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("outside_stands_details", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertTemplateUsed(response, "airport/outside_stands_details.html")

    def test_view_outside_details_stands_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("outside_stands_details", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/outside-stands/{self.outside_stand.pk}/"
        )

    def test_outside_stands_details_id_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("outside_stands_details", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertContains(response, self.outside_stand.id)

    def test_outside_stands_details_size_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("outside_stands_details", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertContains(response, self.outside_stand.size)


class OutsideAircraftStandCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.new_outside_stand_data = {
            "name": "Outside Stand Test",
            "surface": "CON",
            "size": "L",
            "taken": False,
            "airport": self.airport.pk,
        }

    def test_view_outside_stands_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("outside_stands_add"))
        self.assertTemplateUsed(response, "airport/outside_stands_form.html")

    def test_view_outside_stands_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("outside_stands_add"))
        print(response.content)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/outside-stands/new/")

    def test_view_outside_stands_create_creates_new_runway_object(self):
        self.client.force_login(self.user)
        self.assertEqual(OutsideAircraftStand.objects.count(), 0)
        response = self.client.post(
            reverse("outside_stands_add"), self.new_outside_stand_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(OutsideAircraftStand.objects.count(), 1)

    def test_view_outside_stands_create_creates_new_runway_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("outside_stands_add"), self.new_outside_stand_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_outside_stand = OutsideAircraftStand.objects.first()
        self.assertEqual(new_outside_stand.name, "Outside Stand Test")


class OutsideAircraftStandUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_outside_stands_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("outside_stands_update", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertTemplateUsed(response, "airport/outside_stands_form.html")

    def test_view_outside_stands_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Outside Stand Test",
            "surface": self.outside_stand.surface,
            "size": self.outside_stand.size,
            "taken": self.outside_stand.taken,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("outside_stands_update", kwargs={"pk": self.outside_stand.pk}),
            data=update,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.outside_stand.refresh_from_db()
        self.assertEqual(self.outside_stand.name, update["name"])

    def test_view_outside_stands_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("outside_stands_update", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/outside-stands/{self.outside_stand.pk}/update/"
        )


class OutsideAircraftStandDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_outside_stands_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("outside_stands_delete", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertTemplateUsed(response, "airport/outside_stands_delete.html")

    def test_view_outside_stands_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("outside_stands_delete", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/outside-stands/{self.outside_stand.pk}/delete/"
        )

    def test_outside_stands_view_deletes_outside_stands_object(self):
        self.client.force_login(self.user)
        self.assertEqual(OutsideAircraftStand.objects.count(), 1)
        response = self.client.delete(
            reverse("outside_stands_delete", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(OutsideAircraftStand.objects.count(), 0)
