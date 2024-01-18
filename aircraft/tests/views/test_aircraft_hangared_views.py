from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from aircraft.factories import AircraftFactory, AircraftHangaredFactory
from aircraft.models import Aircraft
from aircraft.forms import CreatAircraft


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/1/")


class AircraftsHangaredUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/1/update/")


class AircraftsHangaredCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
        )

    def test_view_aircraft_hangared_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts_hangared_add"))
        self.assertTemplateUsed(response, "aircraft/aircrafts_hangared_form.html")

    def test_view_aircraft_hangared_create_login_required_should_redirect_to_login(
        self,
    ):
        response = self.client.get(reverse("aircrafts_hangared_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts-hangared/new/")


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
