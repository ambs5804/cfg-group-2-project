from classes.recipe import Recipe


def recipe_constructor(data):
    recipes = []
    for recipe in data:
        recipes.append(
            Recipe(recipe['Recipe'], recipe['URL'], recipe['Image'], recipe['Ingredients']))
    return recipes


def make_it_dict(data):
    recipes = []
    for recipe in data:
        recipes.append(recipe.__dict__())
    return recipes
