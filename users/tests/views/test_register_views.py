from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.factories import UserFactory
from organization.factories import CompanyFactory, DepartmentFactory
from users.models import CustomUser


class CustomRegisterViewTest(TestCase):
    def setUp(self) -> None:
        self.company = CompanyFactory.create()
        self.new_user_data_valid = {
            "username": "test_user",
            "email": "test@email.com",
            "password1": "qwert123!",
            "password2": "qwert123!",
            "first_name": "test_name",
            "last_name": "test_name",
            "department": "IT",
            "company": self.company.pk,
        }

        self.new_user_data_invalid = {
            "username": "test user",
            "email": "testemailcom",
            "password1": "123",
            "password2": "qwert123!",
            "first_name": "test_name",
            "last_name": "test_name",
            "department": "IT",
            "company": self.company.pk,
        }

    def test_view_register_uses_correct_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "users/register.html")

    def test_register_view_creates_new_user(self):
        self.assertEqual(CustomUser.objects.count(), 0)
        response = self.client.post(reverse("register"), self.new_user_data_valid)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("login"))
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_register_view_does_not_create_new_user_invalid_data(self):
        self.assertEqual(CustomUser.objects.count(), 0)
        response = self.client.post(reverse("register"), self.new_user_data_invalid)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(CustomUser.objects.count(), 0)
