from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from aircraft.factories import AircraftFactory, AircraftHangaredFactory
from aircraft.models import Aircraft
from http import HTTPStatus


class AircraftView(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create(manufacture="Boeing")
        self.aircraft_hanagared = AircraftHangaredFactory.create(
            outside_stand=None, airport_property=False
        )

    def test_view_aircraft_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        self.assertTemplateUsed(response, "aircraft/aircrafts.html")

    def test_view_aircraft_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("aircrafts"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircrafts/")

    def test_view_aircraft_returns_correct_aircraft_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        self.assertContains(response, "Boeing")

    def test_aircraft_view_displayed_aircrafts_hangared_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        self.assertContains(response, self.aircraft_hanagared.aircraft.name)

    def test_aircraft_view_aircrafts_displayed_hangared_manufacture_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        self.assertContains(response, self.aircraft_hanagared.aircraft.manufacture)


class AircraftsDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create()

    def test_view_aircraft_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertTemplateUsed(response, "aircraft/aircrafts_details.html")

    def test_view_aircraft_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts/1/")

    def test_aircrafts_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.name)

    def test_aircrafts_details_manufacture_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.manufacture)

    def test_aircrafts_details_description_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.description)

    def test_aircrafts_details_fuel_capacity_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.fuel_capacity)

    def test_aircrafts_details_landing_groundroll_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.landing_groundroll)

    def test_aircrafts_details_runway_surface_type_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.runway_surface_type)

    def test_aircrafts_details_take_off_ground_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.take_off_ground)

    def test_aircrafts_details_take_off_over_50ft_distance_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.take_off_over_50ft_distance)

    def test_aircrafts_details_take_off_distance_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_details", kwargs={"pk": self.aircraft.pk})
        )
        self.assertContains(response, self.aircraft.take_off_distance)


class AircraftsUpdateViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create()

    def test_view_aircraft_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_update", kwargs={"pk": self.aircraft.pk})
        )
        self.assertTemplateUsed(response, "aircraft/aircrafts_form.html")

    def test_view_aircraft_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("aircrafts_update", kwargs={"pk": self.aircraft.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts/1/update/")


class AircraftsCreateViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create()

    def test_view_aircraft_add_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts_add"))
        self.assertTemplateUsed(response, "aircraft/aircrafts_form.html")

    def test_view_aircraft_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("aircrafts_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts/new/")


class AircraftsDeleteViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.aircraft = AircraftFactory.create()

    def test_view_aircraft_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("aircrafts_delete", kwargs={"pk": self.aircraft.pk})
        )
        self.assertTemplateUsed(response, "aircraft/aircraft_delete.html")

    def test_view_aircraft_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("aircrafts_delete", kwargs={"pk": self.aircraft.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircrafts/1/delete/")
