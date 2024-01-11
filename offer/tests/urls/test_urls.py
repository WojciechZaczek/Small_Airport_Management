from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from offer.factories import OfferFactory, TrainingFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.offer = OfferFactory.create()
        self.training = TrainingFactory.create()

    def test_offers_url__returns_200_status_code_for_standard_get(self):
        urls = ["offers", "offers_add"]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_offers_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("offers_details", kwargs={"pk": self.offer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_offers_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("offers_update", kwargs={"pk": self.offer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_offers_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("offers_delete", kwargs={"pk": self.offer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_trainings_url_returns_200_status_code_for_standard_get(self):
        urls = ["trainings", "trainings_add"]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_trainings_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("trainings_details", kwargs={"pk": self.training.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_trainings_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("trainings_update", kwargs={"pk": self.training.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_trainings_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("trainings_delete", kwargs={"pk": self.training.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
