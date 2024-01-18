from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from offer.factories import OfferFactory
from airport.factories import AirportFactory


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/offers/")

    def test_view_offers_returns_correct_offer_name_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("offers"))
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/offers/1/")

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
        self.offer = OfferFactory.create(airport=self.airport)

    def test_view_offers_create_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("offers_add"))
        self.assertTemplateUsed(response, "offer/offers_form.html")

    def test_view_offers_create_login_required_should_redirect_to_login(self):
        response = self.client.get(reverse("offers_add"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/offers/new/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/offers/1/update/")


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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/offers/1/delete/")
