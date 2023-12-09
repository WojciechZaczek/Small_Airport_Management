from django.test import TestCase
from ..factories import AircraftFactory, AircraftHangaredFactory
from ..models import Aircraft


class AircraftFactoriesTest(TestCase):
    def test_aircraft_factory_create_object(self):
        AircraftFactory.create()
        self.assertEqual(Aircraft.objects.count(), 1)

    def test_aircraft_factory_create_batch_objects(self):
        AircraftFactory.create_batch(10)
        self.assertEqual(Aircraft.objects.count(), 10)

    def test_aircraft_hangared_factory_create_object(self):
        AircraftHangaredFactory.create()
        self.assertEqual(Aircraft.objects.count(), 1)
