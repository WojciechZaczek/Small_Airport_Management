from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()

    def test_users_urls_returns_200_status_code_for_standard_get(self):
        urls = ["login", "register", "logout", "users"]

        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_users_details_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("users_details", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_users_update_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("users_update", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_users_delete_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("users_delete", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
