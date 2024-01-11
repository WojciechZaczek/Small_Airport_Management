from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from notifications.factories import NotificationFactory


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.notification = NotificationFactory.create()

    def test_notifications_url_returns_200_status_code_for_standard_get(self):
        urls = ["notifications", "notifications_add"]
        for url_name in urls:
            with self.subTest(url_name):
                self.client.force_login(self.user)
                url = reverse(url_name)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_notifications_details_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("notifications_details", kwargs={"pk": self.notification.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_notifications_update_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("notifications_update", kwargs={"pk": self.notification.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_notifications_delete_url_returns_200_status_code_for_standard_get(self):
        self.client.force_login(self.user)
        url = reverse("notifications_delete", kwargs={"pk": self.notification.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
