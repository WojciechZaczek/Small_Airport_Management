from django.test import TestCase, tag
from django.urls import reverse
from users.factories import UserFactory


@tag("x")
class UrlTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create(username="testuser", password="testpassword")

    def test_aircraft_url(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("aircrafts"))
        print(response.content)
        self.assertEqual(response.status_code, 200)
