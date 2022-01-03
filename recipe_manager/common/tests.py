from django.test import TestCase

from common.models import Centiliter, Gram, Kilogram, Liter
from common.services import convert_unit


class ServiceTests(TestCase):

    def test_conversion_of_measurement_unit(self):
        """
        A conversion from one unit from another should return a new unit instance
        with the converted value. Ex: 1 Kg -> 1000 g
        """
        measurement_in_kilograms = Kilogram(1)
        measurement_in_liters = Liter(1)

        measurement_in_grams = convert_unit(measurement_in_kilograms, Gram)
        measurement_in_centiliters = convert_unit(
            measurement_in_liters, Centiliter)

        self.assertEquals(measurement_in_grams.value, 1000)
        self.assertEquals(measurement_in_centiliters.value, 100)

    def test_conversion_between_different_type_of_measurement_units_raise_esception(self):
        """
        A conversion from one unit type (ex: Mass) from another unit type (ex: Volume)
        should raise a TypeError
        """
        with self.assertRaises(TypeError):
            convert_unit(Kilogram(1), Liter)
