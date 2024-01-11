from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from clients.factories import ClientPrivateFactory, ClientCorporateFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.corporate_client = ClientCorporateFactory.create()
        self.private_client = ClientPrivateFactory.create()

    def test_clients_url_returns_200_status_code_for_standard_get(self):
        urls = [
            "clients",
            "clients_add",
            "clients_add_corporate",
            "clients_add_private",
        ]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_clients_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("clients_details", kwargs={"pk": self.private_client.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_clients_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("clients_update", kwargs={"pk": self.private_client.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_clients_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("clients_delete", kwargs={"pk": self.private_client.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
