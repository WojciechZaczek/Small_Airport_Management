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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircrafts/1/update/")

    def test_view_aircraft_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "manufacture": "Example Aircraft Company",
            "name": self.aircraft.name,
            "type": self.aircraft.type,
            "take_off_ground": self.aircraft.take_off_ground,
            "take_off_over_50ft_distance": self.aircraft.take_off_over_50ft_distance,
            "landing_groundroll": self.aircraft.take_off_over_50ft_distance,
            "fuel_capacity": self.aircraft.fuel_capacity,
            "runway_surface_type": self.aircraft.runway_surface_type,
            "description": self.aircraft.description,
        }
        response = self.client.post(
            reverse("aircrafts_update", kwargs={"pk": self.aircraft.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.aircraft.refresh_from_db()
        self.assertEqual(self.aircraft.manufacture, update["manufacture"])


class AircraftsCreateViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.new_aircraft_data = {
            "manufacture": "Example Aircraft Company",
            "name": "Example123",
            "type": "A",
            "take_off_ground": 300,
            "take_off_over_50ft_distance": 500,
            "landing_groundroll": 400,
            "fuel_capacity": 500,
            "runway_surface_type": "CON",
            "description": "Lorem ipsum dolor sit amet",
        }

    def test_view_aircrafts_create_creates_new_runway_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Aircraft.objects.count(), 0)
        response = self.client.post(reverse("aircrafts_add"), self.new_aircraft_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Aircraft.objects.count(), 1)

    def test_view_aircrafts_create_creates_new_aircraft_object_with_correct_content(
        self,
    ):
        self.client.force_login(self.user)
        response = self.client.post(reverse("aircrafts_add"), self.new_aircraft_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_aircraft = Aircraft.objects.first()
        self.assertEqual(new_aircraft.manufacture, "Example Aircraft Company")

    def test_view_aircraft_add_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts_add"))
        self.assertTemplateUsed(response, "aircraft/aircrafts_form.html")

    def test_view_aircraft_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("aircrafts_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/aircrafts/1/delete/")

    def test_aircraft_view_deletes_aircraft_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Aircraft.objects.count(), 1)
        response = self.client.delete(
            reverse("aircrafts_delete", kwargs={"pk": self.aircraft.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Aircraft.objects.count(), 0)
