from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory


class CustomRegisterViewTest(TestCase):
    def test_view_register_uses_correct_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "users/register.html")
