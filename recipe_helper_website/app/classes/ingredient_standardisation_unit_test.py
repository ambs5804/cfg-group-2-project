import unittest
from Recipe_class import Recipe


class TestStandardisedIngredient(unittest.TestCase):
    def test_ingredient1(self):
        # Test case for ingredient with inch measurement
        ingredient = "2 1/2 inch red onion thick slices charred, finely chopped"
        expected = "2 1/2 inch red onion thick slices charred, finely chopped"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient2(self):
        # Test case for ingredient with oz measurement
        ingredient = "120g/4oz plain flour"
        expected = "120g plain flour"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient3(self):
        # Test case for ingredient with cup measurement
        ingredient = "1 cup (140 g) flour, plus more for dusting the onions"
        expected = "1 cup flour, plus more for dusting the onions"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient4(self):
        # Test case for ingredient with multiple measurements
        ingredient = "or 3/4 cup (110 g) flour, plus 1/4 cup (35 g) cornmeal"
        expected = "or 3/4 cup flour, plus 1/4 cup cornmeal"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient5(self):
        # Test case for ingredient with pound measurement
        ingredient = "1 pound frozen peas (3 1/2 cups)"
        expected = "1 pound frozen peas"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient6(self):
        # Test case for ingredient with fraction measurement
        ingredient = "1 /3 cup whole-milk ricotta"
        expected = "1/3 cup whole-milk ricotta"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient7(self):
        # Test case for ingredient with tablespoon measurement
        ingredient = "2 tablespoons unsalted butter"
        expected = "2 tbsp unsalted butter"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient8(self):
        # Test case for ingredient with teaspoon measurement
        ingredient = "1 /2 teaspoon salt"
        expected = "1/2 tsp salt"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient9(self):
        # Test case for ingredient with period in measurement
        ingredient = "1 tsp. ground sumac"
        expected = "1 tsp ground sumac"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient10(self):
        # Test case for ingredient with abbreviation in measurement
        ingredient = "1 tbsp. white pepper"
        expected = "1 tbsp white pepper"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient11(self):
        # Test case for ingredient with fraction in measurement
        ingredient = "1⁄2 cup finely chopped fresh parsley"
        expected = "1/2 cup finely chopped fresh parsley"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient12(self):
        # Test case for ingredient with no measurement
        ingredient = "1 onion, finely chopped"
        expected = "1 onion, finely chopped"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient13(self):
        # Test case for ingredient with None
        ingredient = "None Freshly ground black pepper"
        expected = "Freshly ground black pepper"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient14(self):
        # Test case for ingredient with uni-code fraction in measurement
        ingredient = "¼ cup cilantro, chopped"
        expected = "1/4 cup cilantro, chopped"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient15(self):
        # Test case for ingredient with uni-code fraction in measurement
        ingredient = "1½ lb. whole fish, gutted and cleaned"
        expected = "1 1/2 lb. whole fish, gutted and cleaned"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))

    def test_ingredient16(self):
        # Test case for ingredient with uni-code in ingredient
        ingredient = "1 tablespoon flour – all-purpose"
        expected = "1 tablespoon flour all-purpose"
        self.assertEqual(Recipe._standardise_ingredient(
            (ingredient), expected))


if __name__ == '__main__':
    unittest.main()
