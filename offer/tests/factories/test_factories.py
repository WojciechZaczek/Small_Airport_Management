from django.test import TestCase
from offer.models import Offer, Training
from offer.factories import OfferFactory, TrainingFactory
from airport.models import Airport
from organization.models import Worker


class OfferFactoriesTest(TestCase):
    def test_offer_factory_create_object(self):
        OfferFactory.create()
        self.assertEqual(Offer.objects.count(), 1)

    def test_offer_factory_create_batch_objects(self):
        OfferFactory.create_batch(
            10,
        )
        self.assertEqual(Offer.objects.count(), 10)

    def test_offer_factory_create_airport_subfactory_object(self):
        OfferFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_offer_factory_create_airport_subfactory_batch_objects(self):
        OfferFactory.create_batch(
            10,
        )
        self.assertEqual(Airport.objects.count(), 10)


class TrainingFactoriesTest(TestCase):
    def test_training_factory_create_object(self):
        TrainingFactory.create()
        self.assertEqual(Training.objects.count(), 1)

    def test_training_factory_create_batch_objects(self):
        TrainingFactory.create_batch(
            10,
        )
        self.assertEqual(Training.objects.count(), 10)

    def test_training_factory_create_airport_subfactory_object(self):
        TrainingFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_training_factory_create_airport_subfactory_batch_objects(self):
        TrainingFactory.create_batch(
            10,
        )
        self.assertEqual(Airport.objects.count(), 10)

    def test_training_factory_create_worker_subfactory_object(self):
        TrainingFactory.create()
        self.assertEqual(Worker.objects.count(), 1)

    def test_training_factory_create_worker_subfactory_batch_objects(self):
        TrainingFactory.create_batch(
            10,
        )
        self.assertEqual(Worker.objects.count(), 10)
