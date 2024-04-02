from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from offer.factories import OfferFactory
from airport.factories import AirportFactory
from offer.models import Offer


class OffersViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(name="Offer one", airport=self.airport)

    def test_view_offers_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("offers"))
        self.assertTemplateUsed(response, "offer/offers.html")

    def test_view_offers_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("offers"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/offers/")

    def test_view_offers_returns_correct_offer_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("offers"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Offer one")

    def test_offers_view_displayed_offer_price(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("offers"))
        self.assertContains(response, self.offer.price)


class OffersDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(airport=self.airport)

    def test_view_offers_details_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("offers_details", kwargs={"pk": self.offer.pk})
        )
        self.assertTemplateUsed(response, "offer/offers_details.html")

    def test_view_offers_details_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("offers_details", kwargs={"pk": self.offer.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/offers/{self.offer.pk}/")

    def test_offers_details_name_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("offers_details", kwargs={"pk": self.offer.pk})
        )
        self.assertContains(response, self.offer.name)

    def test_offers_details_price_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("offers_details", kwargs={"pk": self.offer.pk})
        )
        self.assertContains(response, self.offer.price)

    def test_offers_details_description_content_displayed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("offers_details", kwargs={"pk": self.offer.pk})
        )
        self.assertContains(response, self.offer.description)


class OffersCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.new_offer_data = {
            "name": "Alfa Offer",
            "price": 110.00,
            "description": "Test description",
            "airport": self.airport.pk,
        }

    def test_view_offers_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("offers_add"))
        self.assertTemplateUsed(response, "offer/offers_form.html")

    def test_view_offers_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("offers_add"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/offers/new/")

    def test_view_offers_create_creates_new_offer_object(self):
        self.client.force_login(self.user)
        self.assertEqual(Offer.objects.count(), 0)
        response = self.client.post(reverse("offers_add"), self.new_offer_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Offer.objects.count(), 1)

    def test_view_offers_create_creates_new_offer_object_with_correct_content(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("offers_add"), self.new_offer_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        new_offer = Offer.objects.first()
        self.assertEqual(new_offer.name, "Alfa Offer")


class OffersUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(airport=self.airport)

    def test_view_offers_update_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("offers_update", kwargs={"pk": self.offer.pk})
        )
        self.assertTemplateUsed(response, "offer/offers_form.html")

    def test_view_offers_update_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("offers_update", kwargs={"pk": self.offer.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/offers/{self.offer.pk}/update/")

    def test_view_offer_update_changes_object_content(self):
        self.client.force_login(self.user)
        update = {
            "name": "Alfa Offer",
            "price": self.offer.price,
            "description": self.offer.description,
            "airport": self.airport.pk,
        }
        response = self.client.post(
            reverse("offers_update", kwargs={"pk": self.offer.pk}), data=update
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.offer.refresh_from_db()
        self.assertEqual(self.offer.name, update["name"])


class TrainingsDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.airport = AirportFactory.create(company=self.user.company)
        self.offer = OfferFactory.create(airport=self.airport)

    def test_view_offers_delete_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("offers_delete", kwargs={"pk": self.offer.pk})
        )
        self.assertTemplateUsed(response, "offer/offers_delete.html")

    def test_view_offers_delete_login_required_should_redirect_to_login(self):
        response = self.client.get(
            reverse("offers_delete", kwargs={"pk": self.offer.pk})
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, f"/login/?next=/offers/{self.offer.pk}/delete/")
