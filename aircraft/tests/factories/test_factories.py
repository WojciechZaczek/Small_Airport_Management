from django.test import TestCase
from aircraft.factories import AircraftFactory, AircraftHangaredFactory
from aircraft.models import Aircraft, AircraftHangared
from clients.models import Client


class AircraftFactoriesTest(TestCase):
    def test_aircraft_factory_create_object(self):
        AircraftFactory.create()
        self.assertEqual(Aircraft.objects.count(), 1)

    def test_aircraft_factory_create_batch_objects(self):
        AircraftFactory.create_batch(10)
        self.assertEqual(Aircraft.objects.count(), 10)


class AircraftHangaredFactoryTest(TestCase):
    def test_aircraft_hangared_factory_create_object(self):
        AircraftHangaredFactory.create(hangar=None, airport_property=False)
        self.assertEqual(AircraftHangared.objects.count(), 1)

    def test_aircraft_hangared_factory_create_batch_object(self):
        AircraftHangaredFactory.create_batch(10, hangar=None, airport_property=False)
        self.assertEqual(AircraftHangared.objects.count(), 10)

    def test_aircraft_hangared_factory_create_client_subfactory_object(self):
        AircraftHangaredFactory.create(hangar=None, airport_property=False)
        self.assertEqual(Client.objects.count(), 1)

    def test_aircraft_hangared_factory_create_client_subfactory_batch_object(self):
        AircraftHangaredFactory.create_batch(10, hangar=None, airport_property=False)
        self.assertEqual(Client.objects.count(), 10)
