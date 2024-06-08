from classes.Recipe_class import Recipe


def recipe_constructor(data):
    recipes = []
    for recipe in data:
        recipes.append(
            Recipe(recipe['Recipe'], recipe['URL'], recipe['Image'], recipe['Ingredients']))
    return recipes
