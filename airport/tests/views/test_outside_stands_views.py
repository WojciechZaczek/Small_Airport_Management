from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import (
    AirportFactory,
    RunwayFactory,
    HangarFactory,
    OutsideAircraftStandFactory,
)


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/outside-stands/1/")

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
        self.outside_stand = OutsideAircraftStandFactory.create(airport=self.airport)

    def test_view_outside_stands_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("outside_stands_add"))
        self.assertTemplateUsed(response, "airport/outside_stands_form.html")

    def test_view_outside_stands_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("outside_stands_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/outside-stands/new/")


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

    def test_view_outside_stands_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("outside_stands_update", kwargs={"pk": self.outside_stand.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/outside-stands/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/outside-stands/1/delete/")
