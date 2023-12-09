from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from aircraft.factories import *
from clients.factories import ClientFactory
from airport.factories import HangarFactory, OutsideAircraftStandFactory
from unittest import expectedFailure


class AircraftHangaredTest(TestCase):
    def setUp(self) -> None:
        self.aircraft_hangared = AircraftHangaredFactory.create()
        self.airport_client = ClientFactory.create()
        self.airport_hangar = HangarFactory.create()
        self.airport_outside_stand = OutsideAircraftStandFactory.create()

    @expectedFailure
    def test_clean_method_hangar_and_outside_stand(self):
        with self.assertRaises(ValidationError) as context:
            self.aircraft_hangared.clean()
        self.assertIn(
            "Only one of hangar_id or outside_stand_id can be set",
            str(context.exception),
        )

    @expectedFailure
    def test_clean_method_none_hangar_and_none_outside_stand(self):
        self.aircraft_hangared.hangar = None
        self.aircraft_hangared.outside_stand = None
        with self.assertRaises(ValidationError) as context:
            self.aircraft_hangared.clean()
        self.assertIn(
            "At least one of hangar_id or outside_stand_id must be provided",
            str(context.exception),
        )

    @expectedFailure
    def test_clean_method_none_client_and_none_airport_property(self):
        self.aircraft_hangared.airport_property = False
        self.aircraft_hangared.client = None
        with self.assertRaises(ValidationError) as context:
            self.aircraft_hangared.clean()
        self.assertIn(
            "At least one of client_id or airport_property must be provided",
            str(context.exception),
        )

    @expectedFailure
    def test_clean_method_client_and_airport_property(self):
        self.aircraft_hangared.airport_property = True
        with self.assertRaises(ValidationError) as context:
            self.aircraft_hangared.clean()
        self.assertIn(
            "Only on o client_id or airport_property can be set", str(context.exception)
        )
