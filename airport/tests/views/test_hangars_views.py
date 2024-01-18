from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import (
    AirportFactory,
    RunwayFactory,
    HangarFactory,
    OutsideAircraftStandFactory,
)


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/aircraft-stands/")

    def test_view_aircraft_stands_returns_correct_hangar_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hangar one")

    def test_view_aircraft_stands_returns_correct_outside_stand_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Outside stand one")

    def test_view_aircraft_stands_returns_hangar_height_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.hangar.hangar_height)

    def test_view_aircraft_stands_returns_outside_stand_size_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircraft_stands"))
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/hangars/1/")

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
        self.hangar = HangarFactory.create(airport=self.airport)
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_hangars_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("hangars_add"))
        self.assertTemplateUsed(response, "airport/hangars_form.html")

    def test_view_hangars_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("hangars_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/hangars/new/")


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
        self.assertRedirects(response, "/login/?next=/hangars/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/hangars/1/delete/")
