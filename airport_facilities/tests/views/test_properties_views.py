from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport_facilities.factories import PropertyFactory


class PropertiesDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)

    def testproperties_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_details", kwargs={"pk": self.property.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/properties_details.html")

    def test_view_properties_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("properties_details", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/properties/1/")

    def test_properties_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_details", kwargs={"pk": self.property.pk})
        )
        self.assertContains(response, self.property.name)


class PropertiesCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)

    def test_view_properties_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("properties_add"))
        self.assertTemplateUsed(response, "airport_facilities/properties_form.html")

    def test_view_properties_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("properties_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/properties/new/")


class PropertiesUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)

    def test_view_properties_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_update", kwargs={"pk": self.property.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/properties_form.html")

    def test_view_properties_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("properties_update", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/properties/1/update/")


class PropertiesDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.property = PropertyFactory.create(airport=self.airport)

    def test_view_properties_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("properties_delete", kwargs={"pk": self.property.pk})
        )
        self.assertTemplateUsed(response, "airport_facilities/properties_delete.html")

    def test_view_properties_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("properties_delete", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/properties/1/delete/")
