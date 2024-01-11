from django.test import TestCase
from clients.models import Client
from clients.factories import ClientCorporateFactory, ClientPrivateFactory
from organization.models import Company
from offer.models import Training, Offer


class ClientPrivateFactoriesTest(TestCase):
    def test_client_factory_create_object(self):
        ClientPrivateFactory.create()
        self.assertEqual(Client.objects.count(), 1)

    def test_client_factory_create_batch_objects(self):
        ClientPrivateFactory.create_batch(
            10,
        )
        self.assertEqual(Client.objects.count(), 10)

    def test_client_factory_create_company_subfactory_object(self):
        ClientPrivateFactory.create(training=None, offer=None)
        self.assertEqual(Company.objects.count(), 1)

    def test_client_factory_create_company_subfactory_batch_objects(self):
        ClientPrivateFactory.create_batch(10, training=None, offer=None)
        self.assertEqual(Company.objects.count(), 10)

    def test_client_factory_create_training_subfactory_object(self):
        ClientPrivateFactory.create()
        self.assertEqual(Training.objects.count(), 1)

    def test_client_factory_create_training_subfactory_batch_objects(self):
        ClientPrivateFactory.create_batch(10)
        self.assertEqual(Training.objects.count(), 10)

    def test_client_factory_create_offer_subfactory_object(self):
        ClientPrivateFactory.create()
        self.assertEqual(Offer.objects.count(), 1)

    def test_client_factory_create_offer_subfactory_batch_objects(self):
        ClientPrivateFactory.create_batch(10)
        self.assertEqual(Offer.objects.count(), 10)


class ClientCorporateFactoriesTest(TestCase):
    def test_corporate_client_factory_create_object(self):
        ClientCorporateFactory.create()
        self.assertEqual(Client.objects.count(), 1)

    def test_corporate_client_factory_create_batch_objects(self):
        ClientCorporateFactory.create_batch(
            10,
        )
        self.assertEqual(Client.objects.count(), 10)

    def test_corporate_client_factory_create_company_subfactory_object(self):
        ClientCorporateFactory.create(training=None, offer=None)
        self.assertEqual(Company.objects.count(), 1)

    def test_corporate_client_factory_create_company_subfactory_batch_objects(self):
        ClientCorporateFactory.create_batch(10, training=None, offer=None)
        self.assertEqual(Company.objects.count(), 10)

    def test_corporate_client_factory_create_training_subfactory_object(self):
        ClientCorporateFactory.create()
        self.assertEqual(Training.objects.count(), 1)

    def test_corporate_client_factory_create_training_subfactory_batch_objects(self):
        ClientCorporateFactory.create_batch(10)
        self.assertEqual(Training.objects.count(), 10)

    def test_corporate_client_factory_create_offer_subfactory_object(self):
        ClientCorporateFactory.create()
        self.assertEqual(Offer.objects.count(), 1)

    def test_corporate_client_factory_create_offer_subfactory_batch_objects(self):
        ClientCorporateFactory.create_batch(10)
        self.assertEqual(Offer.objects.count(), 10)
