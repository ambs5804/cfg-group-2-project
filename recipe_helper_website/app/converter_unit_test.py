import unittest
from converter import convert_units

#
# class TestUnitConversions(unittest.TestCase):
#     def same_unit_conversion(self):
#         self.assertEqual(convert_units(1, 'cups', 'cups'), "1 cups is equal to 1 cups")
#         self.assertEqual(convert_units(1, 'tsp', 'tsp'), "1 tsp is equal to 1 tsp")
#
#     def different_unit_conversion(self):
#         self.assertEqual(convert_units(1, 'cups', 'tbsp'), "1 cups is equal to 16 tbsp")
#         self.assertEqual(convert_units(2, 'tbsp', 'cups'), "2 tbsp is equal to 0.125 cups")
#         self.assertEqual(convert_units(250, 'g', 'cups'), "250 g is equal to 1.0 cups")
#
#     def zero_unit_conversion(self):
#         self.assertEqual(convert_units(0, 'ml', 'tbsp'), "0 ml is equal to 0 tbsp")
#
#     def invalid_conversion(self):
#         self.assertEqual(convert_units(1, 'g', 'ml'), "Conversion not possible with the provided units.")


import unittest
from converter import convert_units


class TestUnitConversions(unittest.TestCase):

    def test_same_unit_conversion(self):
        self.assertEqual(convert_units(1, 'cups', 'cups'), "1 cups is equal to 1 cups")
        self.assertEqual(convert_units(1, 'tsp', 'tsp'), "1 tsp is equal to 1 tsp")

    def test_different_unit_conversion(self):
        self.assertEqual(convert_units(1, 'cups', 'tbsp'), "1 cups is equal to 16 tbsp")
        self.assertEqual(convert_units(2, 'tbsp', 'cups'), "2 tbsp is equal to 0.125 cups")
        self.assertEqual(convert_units(250, 'g', 'cups'), "250 g is equal to 1.0 cups")

    def test_zero_unit_conversion(self):
        self.assertEqual(convert_units(0, 'ml', 'tbsp'), "0 ml is equal to 0.0 tbsp")

    def test_invalid_conversion(self):
        self.assertEqual(convert_units(1, 'g', 'ml'), "Conversion not possible with the provided units.")

    def test_negative_unit_conversion(self):
        self.assertEqual(convert_units(-1, 'tbsp', 'cups'), "-1 tbsp is equal to -0.0625 cups")


if __name__ == '__main__':
    unittest.main()
