from django.test import TestCase
from django.urls import reverse
from airport.factories import RunwayFactory, AirportFactory


class RunwayModelTest(TestCase):
    def setUp(self) -> None:
        self.runway = RunwayFactory.create()
        self.airport = AirportFactory.create()

    def test_TODA_with_CWY_equals_zero(self):
        self.runway.CWY = 0
        self.runway.TORA = 500
        expected_TODA = self.runway.TORA
        self.assertEqual(self.runway.TODA, expected_TODA)

    def test_TODA_with_CWY_greater_than_zero(self):
        self.runway.CWY = 500
        self.runway.TORA = 500
        expected_TODA = self.runway.CWY + self.runway.TORA
        self.assertEqual(self.runway.TODA, expected_TODA)

    def test_ASDA_with_SWY_equals_zero(self):
        self.runway.SWY = 0
        self.runway.TORA = 500
        expected_ASDA = self.runway.TORA
        self.assertEqual(self.runway.ASDA, expected_ASDA)

    def test_ASDA_with_SWY_greater_than_zero(self):
        self.runway.SWY = 500
        self.runway.TORA = 500
        expected_ASDA = self.runway.SWY + self.runway.TORA
        self.assertEqual(self.runway.ASDA, expected_ASDA)
