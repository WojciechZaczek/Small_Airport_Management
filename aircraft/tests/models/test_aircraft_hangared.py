from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from aircraft.factories import AircraftHangaredFactory


class AircraftHangaredModelTest(TestCase):
    def test_clean_method_hangar_and_outside_stand_return_error(self):
        aircraft_hangared = AircraftHangaredFactory.build()
        with self.assertRaises(ValidationError) as context:
            aircraft_hangared.clean()

        self.assertIn(
            "Only one of hangar_id or outside_stand_id can be set",
            str(context.exception),
        )

    def test_clean_method_none_hangar_and_none_outside_stand_return_error(self):
        aircraft_hangared = AircraftHangaredFactory.build(
            hangar=None, outside_stand=None
        )
        with self.assertRaises(ValidationError) as context:
            aircraft_hangared.clean()

        self.assertIn(
            "At least one of hangar_id or outside_stand_id must be provided",
            str(context.exception),
        )

    def test_clean_method_none_client_and_none_airport_property_return_error(self):
        aircraft_hangared = AircraftHangaredFactory.build(
            hangar=None, client=None, airport_property=False
        )
        with self.assertRaises(ValidationError) as context:
            aircraft_hangared.clean()
        self.assertIn(
            "At least one of client_id or airport_property must be provided",
            str(context.exception),
        )

    def test_clean_method_client_and_airport_property_return_error(self):
        aircraft_hangared = AircraftHangaredFactory.build(
            hangar=None, airport_property=True
        )
        with self.assertRaises(ValidationError) as context:
            aircraft_hangared.clean()
        self.assertIn(
            "Only on of client_id or airport_property can be set",
            str(context.exception),
        )
