from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import (
    AirportFactory,
    RunwayFactory,
    HangarFactory,
    OutsideAircraftStandFactory,
)


class RunwaysListViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.runway = RunwayFactory.create(name="One", airport=self.airport)

    def test_view_runways_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("runways"))
        self.assertTemplateUsed(response, "airport/runways.html")

    def test_view_runways_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("runways"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/runways/")

    def test_view_runways_returns_correct_runway_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("runways"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "One")

    def test_runways_view_displayed_runway_length_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("runways"))
        self.assertContains(response, self.runway.length)


class RunwaysDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.runway = RunwayFactory.create(airport=self.airport)

    def test_view_runways_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertTemplateUsed(response, "airport/runways_details.html")

    def test_view_runways_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/runways/1/")

    def test_runways_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.name)

    def test_runways_details_length_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.length)

    def test_runways_details_width_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.width)

    def test_runways_details_TORA_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.TORA)

    def test_runways_details_TODA_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.TODA)

    def test_runways_details_CWY_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.CWY)

    def test_runways_details_SWY_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.SWY)

    def test_runways_details_TODA_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.TODA)

    def test_runways_details_ASDA_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_details", kwargs={"pk": self.runway.pk})
        )
        self.assertContains(response, self.runway.ASDA)


class RunwaysCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.runway = RunwayFactory.create(airport=self.airport)

    def test_view_runways_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("runways_add"))
        self.assertTemplateUsed(response, "airport/runways_form.html")

    def test_view_runways_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("runways_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/runways/new/")


class RunwaysUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.runway = RunwayFactory.create(airport=self.airport)

    def test_view_runways_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_update", kwargs={"pk": self.runway.pk})
        )
        self.assertTemplateUsed(response, "airport/runways_form.html")

    def test_view_runways_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("runways_update", kwargs={"pk": self.runway.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/runways/1/update/")


class RunwaysDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.runway = RunwayFactory.create(airport=self.airport)

    def test_view_runways_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("runways_delete", kwargs={"pk": self.runway.pk})
        )
        self.assertTemplateUsed(response, "airport/runways_delete.html")

    def test_view_runways_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("runways_delete", kwargs={"pk": self.runway.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/runways/1/delete/")
