from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import OthersFactory


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/others/1/")

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
        self.other = OthersFactory.create(airport=self.airport)

    def test_view_others_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("others_add"))
        self.assertTemplateUsed(response, "airport_facilities/others_form.html")

    def test_view_others_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("others_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/others/new/")


class OthersUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/others/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/others/1/delete/")
