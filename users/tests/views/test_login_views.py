from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from users.models import CustomUser
from organization.factories import CompanyFactory
from django.contrib.auth.hashers import make_password


class CustomLoginViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.user = UserFactory.create(
            username="test_user",
            password=make_password("qwerty123!"),
            company=self.company,
        )
        self.valid_data = {"username": "test_user", "password": "qwerty123!"}
        self.invalid_data = {"username": "test_user", "password": "wrong_password"}

    def test_view_login_uses_correct_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "users/login.html")

    def test_view_logout_uses_correct_template(self):
        response = self.client.get(reverse("logout"))
        self.assertTemplateUsed(response, "users/logout.html")

    def test_login_view_returns_success(self):
        response = self.client.post(reverse("login"), data=self.valid_data)
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
