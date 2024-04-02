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
from airport.models import Hangar


class AircraftStandsViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.hangar = HangarFactory.create(airport=self.airport, name="Hangar one")
        self.outside_stand = OutsideAircraftStandFactory.create(
            airport=self.airport, name="Outside stand one"
        )

    def test_view_aircraft_stands_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertTemplateUsed(response, "airport/aircraft_stands.html")

    def test_view_aircraft_stands_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircraft-stands/")

    def test_view_aircraft_stands_returns_correct_hangar_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Hangar one")

    def test_view_aircraft_stands_returns_correct_outside_stand_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Outside stand one")

    def test_view_aircraft_stands_returns_hangar_height_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.hangar.hangar_height)

    def test_view_aircraft_stands_returns_outside_stand_size_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.outside_stand.size)


class HangarsDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.hangar = HangarFactory.create(airport=self.airport)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_hangars_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertTemplateUsed(response, "airport/hangars_details.html")

    def test_view_hangars_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/hangars/{self.hangar.pk}/")

    def test_hangar_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.name)

    def test_hangar_details_hangar_wight_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.hangar_wight)

    def test_hangar_details_hangar_height_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.hangar_height)

    def test_hangar_details_doors_height_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.doors_height)

    def test_hangar_details_doors_wight_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.doors_wight)

    def test_hangar_details_small_stands_no_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.small_stands_no)

    def test_hangar_details_small_stands_taken_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_details", kwargs={"pk": self.hangar.pk})
        )
        self.assertContains(response, self.hangar.small_stands_taken)


class HangarsCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.new_hangar_data = {
            "name": "Hangar Test",
            "hangar_height": 10.5,
            "hangar_wight": 25.0,
            "doors_height": 8.0,
            "doors_wight": 20.0,
            "small_stands_no": 15,
            "small_stands_taken": 5,
            "airport": self.airport.pk,
        }

    def test_view_hangars_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("hangars_add"))
        self.assertTemplateUsed(response, "airport/hangars_form.html")

    def test_view_hangars_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("hangars_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/hangars/new/")

    def test_view_hangars_create_creates_new_runway_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Hangar.objects.count(), 0)
        response = self.client.post(reverse("hangars_add"), self.new_hangar_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Hangar.objects.count(), 1)

    def test_view_hangars_create_creates_new_runway_object_with_correct_content(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("hangars_add"), self.new_hangar_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_hangar = Hangar.objects.first()
        self.assertEqual(new_hangar.name, "Hangar Test")


class HangarsUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.hangar = HangarFactory.create(airport=self.airport)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_hangars_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_update", kwargs={"pk": self.hangar.pk})
        )
        self.assertTemplateUsed(response, "airport/hangars_form.html")

    def test_view_hangars_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("hangars_update", kwargs={"pk": self.hangar.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f"/login/?next=/hangars/{self.hangar.pk}/update/"
        )

    def test_view_hangars_update_changes_object_content(self):
        self.client.force_login(self.user)
        data_update = {
            "name": "Test Hangar",
            "hangar_height": self.hangar.hangar_height,
            "hangar_wight": self.hangar.hangar_wight,
            "doors_height": self.hangar.doors_height,
            "doors_wight": self.hangar.doors_wight,
            "small_stands_no": self.hangar.small_stands_no,
            "small_stands_taken": self.hangar.small_stands_taken,
            "airport": self.hangar.airport.pk,
        }

        response = self.client.post(
            reverse("hangars_update", kwargs={"pk": self.hangar.pk}), data_update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.hangar.refresh_from_db()
        self.assertEqual(self.hangar.name, "Test Hangar")


class HangarsDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.hangar = HangarFactory.create(airport=self.airport)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_hangars_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("hangars_delete", kwargs={"pk": self.hangar.pk})
        )
        self.assertTemplateUsed(response, "airport/hangars_delete.html")

    def test_view_hangars_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("hangars_delete", kwargs={"pk": self.hangar.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/hangars/{self.hangar.pk}/delete/"
        )

    def test_hangars_view_deletes_hangar_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Hangar.objects.count(), 1)
        response = self.client.delete(
            reverse("hangars_delete", kwargs={"pk": self.hangar.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Hangar.objects.count(), 0)
