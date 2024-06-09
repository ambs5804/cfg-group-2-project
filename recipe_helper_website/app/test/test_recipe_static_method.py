import unittest
from recipe_static_method import standardise_ingredient


# There was no way to test this static function while it was insided the class without affecting the ability of the app to run. The imports of classes for the app need to be listed as (e.g. from classes.ingredeient import ingredient) but when running a testing suite, it would return an error with this import file path - therfore a separte version of the function is used. This function is a static method in recipe that standardises the ingredients provided in the mapped api data.

class TestUnitConversions(unittest.TestCase):

    def test_ingredient_standarisation(self):
        ingredient = "2 1/2 inch red onion thick slices charred, finely chopped"
        expected = "2 1/2 inch red onion thick slices charred, finely chopped"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation2(self):
        ingredient = "120g/4oz plain flour"
        expected = "120g plain flour"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation3(self):
        ingredient = "1 cup (140 g) flour, plus more for dusting the onions"
        expected = "1 cup flour, plus more for dusting the onions"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    # Test case for ingredient with multiple measurements
    def test_ingredient_standarisation4(self):
        ingredient = "or 3/4 cup (110 g) flour, plus 1/4 cup (35 g) cornmeal"
        expected = "or 3/4 cup flour, plus 1/4 cup cornmeal"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation5(self):
        ingredient = "1 pound frozen peas (3 1/2 cups)"
        expected = "1 pound frozen peas"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation6(self):
        ingredient = "1 /3 cup whole-milk ricotta"
        expected = "1/3 cup whole-milk ricotta"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation7(self):
        ingredient = "2 tablespoons unsalted butter"
        expected = "2 tbsp unsalted butter"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation8(self):
        ingredient = "1 /2 teaspoon salt"
        expected = "1/2 tsp salt"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation9(self):
        ingredient = "1 tsp. ground sumac"
        expected = "1 tsp ground sumac"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation10(self):
        ingredient = "1 tbsp. white pepper"
        expected = "1 tbsp white pepper"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation11(self):
        ingredient = "1⁄2 cup finely chopped fresh parsley"
        expected = "1/2 cup finely chopped fresh parsley"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation12(self):
        ingredient = "1 onion, finely chopped"
        expected = "1 onion, finely chopped"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation13(self):
        ingredient = "None Freshly ground black pepper"
        expected = "Freshly ground black pepper"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation14(self):
        ingredient = "¼ cup cilantro, chopped"
        expected = "1/4 cup cilantro, chopped"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)

    def test_ingredient_standarisation15(self):
        ingredient = "1 tablespoon flour – all-purpose"
        expected = "1 tbsp flour all-purpose"
        result = standardise_ingredient(ingredient)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
