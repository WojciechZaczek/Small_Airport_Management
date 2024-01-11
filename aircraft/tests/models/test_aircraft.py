from django.test import TestCase
from django.urls import reverse
from aircraft.factories import AircraftFactory
from airport.factories import RunwayFactory


class AircraftModelTest(TestCase):
    def setUp(self):
        self.aircraft = AircraftFactory.create()
        self.runway = RunwayFactory.create()

    def test_take_off_distance_works_property(self):
        expected_take_off_distance = (
            self.aircraft.take_off_ground + self.aircraft.take_off_over_50ft_distance
        )
        self.assertEqual(self.aircraft.take_off_distance, expected_take_off_distance)

    def test_can_land_at_airport_positive(self):
        self.runway.LDA = 600
        self.aircraft.landing_groundroll = 350
        self.assertTrue(self.aircraft.can_land_at_airport([self.runway]))

    def test_can_land_at_airport_negative(self):
        self.runway.LDA = 300
        self.aircraft.landing_groundroll = 350
        self.assertFalse(self.aircraft.can_land_at_airport([self.runway]))
