import re

from classes.Ingredient_class import Ingredient

from classes.Id_assigner import ID

pattern1 = re.compile(r"(\d+\s?\w+)\/\d+\w+", re.MULTILINE)
# brackets  (3 1/2 cups)
pattern2 = re.compile(
    r"\s\(\d+.?\s?\w+(\/\d+\s?\w+)?\)", re.MULTILINE)
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
# U+00BC 1⁄4
pattern10 = re.compile(r"\u00BC")
# 1⁄2
pattern11 = re.compile(r"\u00bd")
# None
pattern12 = re.compile(r"None")
# digit 1⁄2
pattern13 = re.compile(r"(\d+)\u00bd")
# digit 1⁄4
pattern14 = re.compile(r"(\d+)\u00BC")
# unicode -
pattern15 = re.compile(r"\s?\u2013\s?")


class Recipe:

    def __init__(self, title, url, img, ingredients):
        self.id = ID.make_id()
        self.title = title
        self.url = url
        self.img = img
        self.ingredients = Recipe._standardise_ingredients(ingredients)

    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "img": self.img,
            "ingredients": [ingredient.__dict__() for ingredient in self.ingredients]
        }

  # debugging
    def __str__(self):
        return f"{self.id} - {self.title} - {self.url} - {self.img} - {self.ingredients}"

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
        substitution10 = "1/4"
        substitution11 = "1/2"
        substitution12 = "\1 1/2"
        substitution13 = "\1 1/4"
        substitution14 = " "

        #
        standardised = re.sub(patter6, substitution6, ingredient, 0)
        standardised = re.sub(pattern10, substitution10, standardised, 0)
        standardised = re.sub(
            pattern11, substitution11, standardised, 0)
        standardised = re.sub(
            pattern12, substitution2, standardised, 0)
        standardised = re.sub(pattern13, substitution12, standardised, 0)
        standardised = re.sub(pattern14, substitution13, standardised, 0)
        standardised = re.sub(pattern15, substitution14, standardised, 0)
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
