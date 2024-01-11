from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from airport.factories import HangarFactory


class HangarModelTest(TestCase):
    def test_hangar_clean_method_stands_no_smaller_than_stands_taken_return_error(self):
        hangar = HangarFactory.build(small_stands_no=0, small_stands_taken=1)
        with self.assertRaises(ValidationError) as context:
            hangar.clean()
        self.assertIn("Not enough free stands", str(context.exception))
