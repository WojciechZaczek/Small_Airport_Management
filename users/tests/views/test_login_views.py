from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory


class CustomLoginViewTest(TestCase):
    def test_view_login_uses_correct_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "users/login.html")

    def test_view_logout_uses_correct_template(self):
        response = self.client.get(reverse("logout"))
        self.assertTemplateUsed(response, "users/logout.html")
