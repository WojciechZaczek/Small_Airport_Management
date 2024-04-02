from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from airport.factories import AirportFactory
from airport.models import Airport
from organization.factories import CompanyFactory


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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
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
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(company=self.company)
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
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/airports/{self.airport.pk}/update/"
        )

    def test_view_airport_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Test name",
            "city": self.airport.city,
            "address": self.airport.address,
            "contact": self.airport.contact,
            "types_of_traffic_permitted": self.airport.types_of_traffic_permitted,
            "radio": self.airport.radio,
            "elevation": self.airport.elevation,
            "co_ordinates": self.airport.co_ordinates,
            "description": self.airport.description,
            "length": self.airport.length,
            "width": self.airport.width,
            "square_meters": self.airport.square_meters,
            "company": self.company.pk,
        }
        response = self.client.post(
            reverse("airports_update", kwargs={"pk": self.airport.pk}), data=update
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.airport.refresh_from_db()
        self.assertEqual(self.airport.name, update["name"])


class AirportCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.new_airport_data = {
            "name": "Test name",
            "city": "city",
            "address": "address",
            "contact": "test contact",
            "types_of_traffic_permitted": "IFR",
            "radio": 10,
            "elevation": 10,
            "co_ordinates": "1212",
            "description": "test description",
            "length": 100,
            "width": 100,
            "square_meters": 100,
            "AIP": "",
            "company": self.user.company.pk,
        }

    def test_view_airport_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("airports_add"))
        self.assertTemplateUsed(response, "airport/airport_form.html")

    def test_view_airport_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("airports_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/airports/new/")

    def test_view_runways_create_creates_new_runway_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Airport.objects.count(), 0)
        response = self.client.post(reverse("airports_add"), self.new_airport_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Airport.objects.count(), 1)

    def test_view_airport_create_creates_new_runway_object_with_correct_content(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("airports_add"), self.new_airport_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_airport = Airport.objects.first()
        self.assertEqual(new_airport.name, "Test name")


class AirportDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)

    def test_view_airport_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("airports_delete", kwargs={"pk": self.airport.pk})
        )
        self.assertTemplateUsed(response, "airport/airport_delete.html")

    def test_view_airport_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("airports_delete", kwargs={"pk": self.airport.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, f"/login/?next=/airports/{self.airport.pk}/delete/"
        )

    def test_airport_delete_view_deletes_airport_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Airport.objects.count(), 1)
        response = self.client.delete(
            reverse("airports_delete", kwargs={"pk": self.airport.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Airport.objects.count(), 0)
