from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from clients.factories import ClientPrivateFactory, ClientCorporateFactory


class ClientModelTest(TestCase):
    def setUp(self) -> None:
        self.corporate_client = ClientCorporateFactory.create()
        self.private_client = ClientPrivateFactory.create()

    def test_str_for_corporate_client(self):
        expected_str = str(self.corporate_client)
        self.assertEqual(f"{self.corporate_client.company_name}", expected_str)

    def test_str_for_private_client(self):
        expected_str = str(self.private_client)
        self.assertEqual(
            f"{self.private_client.name} {self.private_client.last_name}", expected_str
        )
