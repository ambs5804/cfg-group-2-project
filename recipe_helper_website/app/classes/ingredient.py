import re

# find all units
unit_pattern = r"(cup|oz|ml|kg|tsp|tbsp|cups|fl oz)"


class Ingredient():

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

    def __dict__(self):
        return {
            "quantity": self.quantity,
            "unit": self.unit,
            "item": self.item,
            "convertable": self.convertable
        }

    def __repr__(self):
        return f"{self.quantity},{self.unit},{self.item},{self.convertable}"
