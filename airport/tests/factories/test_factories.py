from django.test import TestCase
from airport.models import Airport, Runway, OutsideAircraftStand, Hangar
from airport.factories import (
    AirportFactory,
    RunwayFactory,
    HangarFactory,
    OutsideAircraftStandFactory,
)
from organization.models import Company


class AirportFactoriesTest(TestCase):
    def test_airport_factory_create_object(self):
        AirportFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_airport_factory_create_batch_objects(self):
        AirportFactory.create_batch(10)
        self.assertEqual(Airport.objects.count(), 10)

    def test_airport_factory_create_company_subfactory_object(self):
        AirportFactory.create()
        self.assertEqual(Company.objects.count(), 1)

    def test_airport_factory_create_company_subfactory_batch_objects(self):
        AirportFactory.create_batch(10)
        self.assertEqual(Company.objects.count(), 10)


class RunwayFactoriesTest(TestCase):
    def test_runway_factory_create_object(self):
        RunwayFactory.create()
        self.assertEqual(Runway.objects.count(), 1)

    def test_runway_factory_create_batch_objects(self):
        RunwayFactory.create_batch(10)
        self.assertEqual(Runway.objects.count(), 10)

    def test_runway_factory_create_airport_subfactory_object(self):
        RunwayFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_runway_factory_create_airport_subfactory_batch_objects(self):
        RunwayFactory.create_batch(10)
        self.assertEqual(Airport.objects.count(), 10)


class HangarFactoriesTest(TestCase):
    def test_hangar_factory_create_object(self):
        HangarFactory.create()
        self.assertEqual(Hangar.objects.count(), 1)

    def test_hangar_factory_create_batch_objects(self):
        HangarFactory.create_batch(10)
        self.assertEqual(Hangar.objects.count(), 10)

    def test_hangar_factory_create_airport_subfactory_object(self):
        HangarFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_hangar_factory_create_airport_subfactory_batch_objects(self):
        HangarFactory.create_batch(10)
        self.assertEqual(Airport.objects.count(), 10)


class OutsideAircraftStandFactoriesTest(TestCase):
    def test_outside_stand_factory_create_object(self):
        OutsideAircraftStandFactory.create()
        self.assertEqual(OutsideAircraftStand.objects.count(), 1)

    def test_outside_stand_factory_create_batch_objects(self):
        OutsideAircraftStandFactory.create_batch(10)
        self.assertEqual(OutsideAircraftStand.objects.count(), 10)

    def test_outside_stand_factory_create_airport_subfactory_object(self):
        OutsideAircraftStandFactory.create()
        self.assertEqual(Airport.objects.count(), 1)

    def test_outside_stand_factory_create_airport_subfactory_batch_objects(self):
        OutsideAircraftStandFactory.create_batch(10)
        self.assertEqual(Airport.objects.count(), 10)
