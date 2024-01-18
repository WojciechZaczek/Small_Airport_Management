from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from airport.factories import AirportFactory


class AirportListViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(name="London", company=self.user.company)

    def test_view_airport_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertTemplateUsed(response, "airport/airport.html")

    def test_view_airport_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("airports"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/airports/")

    def test_view_airport_returns_correct_aircraft_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, "London")

    def test_airport_view_displayed_airport_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.name)

    def test_airport_view_airport_displayed_airport_company(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.company)

    def test_airport_view_airport_displayed_airport_city(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.city)

    def test_airport_view_airport_displayed_airport_address(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.address)

    def test_airport_view_airport_displayed_airport_contact(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.contact)

    def test_airport_view_airport_displayed_airport_description(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.description)

    def test_airport_view_airport_displayed_airport_types_of_traffic_permitted(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.types_of_traffic_permitted)

    def test_airport_view_airport_displayed_airport_radio(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.radio)

    def test_airport_view_airport_displayed_airport_co_ordinates(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.co_ordinates)

    def test_airport_view_airport_displayed_airport_elevation(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.elevation)

    def test_airport_view_airport_displayed_airport_length(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.length)

    def test_airport_view_airport_displayed_airport_width(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.width)

    def test_airport_view_airport_displayed_airport_square_meters(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports"))
        self.assertContains(response, self.airport.square_meters)


class AirportUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)

    def test_view_airport_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("airports_update", kwargs={"pk": self.airport.pk})
        )
        self.assertTemplateUsed(response, "airport/airport_form.html")

    def test_view_airport_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("airports_update", kwargs={"pk": self.airport.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/airports/1/update/")
