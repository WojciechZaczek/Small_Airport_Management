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

    def test_corporate_client_clean_no_company_name_return_error(self):
        client = ClientCorporateFactory.build(company_name=None)
        with self.assertRaises(ValidationError) as context:
            client.clean()
        self.assertIn("Corporate name must be provided", str(context.exception))

    def test_corporate_client_clean_no_nip_return_error(self):
        client = ClientCorporateFactory.build(nip=None)
        with self.assertRaises(ValidationError) as context:
            client.clean()
        self.assertIn("NIP must be provided", str(context.exception))

    def test_private_client_clean_no_name_return_error(self):
        client = ClientPrivateFactory.build(name=None)
        with self.assertRaises(ValidationError) as context:
            client.clean()
        self.assertIn("Name must be provided", str(context.exception))

    def test_private_client_clean_no_last_name_return_error(self):
        client = ClientPrivateFactory.build(last_name=None)
        with self.assertRaises(ValidationError) as context:
            client.clean()
        self.assertIn("Last name must be provided", str(context.exception))

    def test_private_client_clean_no_pesel_return_error(self):
        client = ClientPrivateFactory.build(pesel=None)
        with self.assertRaises(ValidationError) as context:
            client.clean()
        self.assertIn("Pesel must be provided", str(context.exception))
