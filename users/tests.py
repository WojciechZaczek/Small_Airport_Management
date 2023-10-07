from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import CustomUser
from organization.models import Company

User = get_user_model()
TestCompany = Company()


class TestLoginView(TestCase):
    def setUp(self):
        self.login_url = reverse("login")
        self.credentials = {
            "username": "testuser",
            "password": "testpassword",
            "company_id": TestCompany.id,
        }

        self.user = User.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(self.login_url, data=self.credentials, follow=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(response.context["user"].is_authenticated)
