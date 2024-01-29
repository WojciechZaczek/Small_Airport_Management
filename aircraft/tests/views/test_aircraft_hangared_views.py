from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import AirportFactory, OutsideAircraftStandFactory, HangarFactory
from aircraft.factories import AircraftFactory, AircraftHangaredFactory
from aircraft.models import AircraftHangared


class AircraftsHangaredDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
        )

    def test_view_aircraft_hangared_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse(
                "aircrafts_hangared_details", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertTemplateUsed(response, "aircraft/aircrafts_hangared_details.html")

    def test_view_aircraft_hangared_details_login_required_should_redirect_to_login(
        self,
    ):
        response = self.client.get(
            reverse(
                "aircrafts_hangared_details", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/1/")


class AircraftsHangaredUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.hangar = HangarFactory.create(airport=self.airport)
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            airport=self.airport, outside_stand=None, airport_property=False
        )

    def test_view_aircraft_hangared_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse(
                "aircrafts_hangared_update", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertTemplateUsed(response, "aircraft/aircrafts_hangared_form.html")

    def test_view_aircraft_hangared_update_login_required_should_redirect_to_login(
        self,
    ):
        response = self.client.get(
            reverse(
                "aircrafts_hangared_update", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/1/update/")

    def test_view_aircraft_hangared_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "aircraft": self.aircraft.pk,
            "aircraft_registration_no": "Test ABC123",
            "airport_property": True,
            "hangar": self.hangar.pk,
            "airport": self.airport.pk,
        }

        response = self.client.post(
            reverse(
                "aircrafts_hangared_update", kwargs={"pk": self.aircraft_hanagared.pk}
            ),
            data=update,
        )
        # form = response.context['form']
        # print(form.is_valid())
        # print(form.errors)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.aircraft_hanagared.refresh_from_db()
        self.assertEqual(
            self.aircraft_hanagared.aircraft_registration_no,
            update["aircraft_registration_no"],
        )


class AircraftsHangaredCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.aircraft = AircraftFactory.create()
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)
        self.hangar = HangarFactory.create()
        self.aircraft_hanagared_data = {
            "aircraft": self.aircraft.pk,
            "aircraft_registration_no": "Test ABC123",
            "airport_property": True,
            "outside_stand": self.outside_stand.pk,
            "airport": self.airport.pk,
        }

    def test_view_aircraft_hangared_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts_hangared_add"))
        self.assertTemplateUsed(response, "aircraft/aircrafts_hangared_form.html")

    def test_view_aircraft_hangared_create_login_required_should_redirect_to_login(
        self,
    ):
        response = self.client.get(reverse("aircrafts_hangared_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/new/")

    def test_view_aircraft_hangared_create_creates_new_aircraft_hangared_object(self):
        self.client.force_login(self.user)
        self.assertEqual(AircraftHangared.objects.count(), 0)
        response = self.client.post(
            reverse("aircrafts_hangared_add"), self.aircraft_hanagared_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(AircraftHangared.objects.count(), 1)

    def test_view_aircraft_hangared_creates_new_aircraft_hangared_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("aircrafts_hangared_add"), self.aircraft_hanagared_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_aircraft_hanagared = AircraftHangared.objects.first()
        self.assertEqual(new_aircraft_hanagared.aircraft_registration_no, "Test ABC123")


class AircraftsHangaredDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
        )

    def test_view_aircraft_hangared_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse(
                "aircrafts_hangared_delete", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertTemplateUsed(response, "aircraft/aircrafts_hangared_delete.html")

    def test_view_aircraft_hangared_delete_login_required_should_redirect_to_login(
        self,
    ):
        response = self.client.get(
            reverse(
                "aircrafts_hangared_delete", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/1/delete/")

    def test_aircraft_hangared_view_deletes_runway_object(self):
        self.client.force_login(self.user)
        self.assertEqual(AircraftHangared.objects.count(), 1)
        response = self.client.delete(
            reverse(
                "aircrafts_hangared_delete", kwargs={"pk": self.aircraft_hanagared.pk}
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(AircraftHangared.objects.count(), 0)
