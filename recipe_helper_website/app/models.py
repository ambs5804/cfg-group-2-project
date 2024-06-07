import re

from Id_assigner import ID
# find all units
unit_pattern = r"(cup|oz|ml|kg|tsp|tbsp|cups|fl oz)"
#
pattern1 = re.compile(r"(\d+\s?\w+)\/\d+\w+", re.MULTILINE)
# brackets  (3 1/2 cups)
pattern2 = re.compile(
    r"\s\(\d+.?\s?\w+(\/\d+\s?\w+)?\)", re.MULTILINE,)
# 1 /3
pattern3 = re.compile(r"(\d+)\s?(\/\d)")
# tablespoon, tbsp., Tbsp., Tbsp
pattern4 = re.compile(r"tablespoons?|tbsp\.", re.IGNORECASE)
# teaspoon, tsp., Tsp., Tsp
pattern5 = re.compile(r"teaspoons?|tsp\.", re.IGNORECASE)
# 1⁄2
patter6 = re.compile(r"(\d+)\u2044(\d+)")
# grams, Grams
pattern7 = re.compile(r"grams?|Grams?", re.IGNORECASE)
# millilitres, ML
pattern8 = re.compile(r"millilitres?|ML", re.IGNORECASE)
# ounces, OZ
pattern9 = re.compile(r"ounces?|OZ", re.IGNORECASE)


class Recipe:
    def __init__(self, title, url, ingredients):
        self.id = ID().make_id()
        self.title = title
        self.url = url
        self.ingredients = Recipe._standardise_ingredients(ingredients)

  # debugging
    def __str__(self):
        return f"{self.id} - {self.title} - {self.url} - {self.ingredients}"

    @staticmethod
    def _standardise_ingredients(ingredients):
        standardised_ingredients = []
        for ingredient in ingredients:
            standardised_ingredients.append(
                Recipe._standardise_ingredient(ingredient))
        return standardised_ingredients

    @staticmethod
    def _standardise_ingredient(ingredient):
        substitution = r"\1"
        substitution2 = ""
        substitution3 = r"\1\2"
        substitution4 = "tbsp"
        substitution5 = "tsp"
        substitution6 = r"\1/\2"
        substitution7 = "g"
        substitution8 = "ml"
        substitution9 = "oz"
        #
        standardised = re.sub(patter6, substitution6, ingredient, 0)
        standardised = re.sub(
            pattern1, substitution, standardised, 0)
        standardised = re.sub(
            pattern2, substitution2, standardised, 0)
        standardised = re.sub(pattern3, substitution3, standardised, 0)
        standardised = re.sub(pattern4, substitution4, standardised, 0)
        standardised = re.sub(pattern5, substitution5, standardised, 0)
        standardised = re.sub(pattern7, substitution7, standardised, 0)
        standardised = re.sub(pattern8, substitution8, standardised, 0)
        standardised = re.sub(pattern9, substitution9, standardised, 0)

        return Ingredient(standardised)


class Ingredient:

    def __init__(self, ingredient):
        if bool(re.search(unit_pattern, ingredient)):
            self.convertable = True
            split = re.split(unit_pattern, ingredient, maxsplit=1, flags=re.I)
            self.quantity = split[0]
            self.unit = split[1]
            self.item = split[2]
        else:
            self.quantity = None
            self.unit = None
            self.item = ingredient
            self.convertable = False

    def __repr__(self):
        return f"{self.quantity} - {self.unit} - {self.item} - {self.convertable}"
