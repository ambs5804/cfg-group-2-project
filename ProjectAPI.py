import requests
import csv


def recipe_search(ingredient):
    app_id = 'ac2be905'  #  Edamam API app ID
    app_key = '0809ac9cd1c28ee2e43b387a5c182265'  # Edamam API app key
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']


def save_to_csv(recipes, ingredient):
    if recipes:
        file_name = f"{ingredient}_recipes.csv"

        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Recipe', 'URL', 'Ingredients'])

            for recipe in recipes:
                recipe_info = recipe['recipe']
                recipe_name = recipe_info['label']
                recipe_url = recipe_info['url']
                ingredients = "\n".join(recipe_info['ingredientLines'])
                writer.writerow([recipe_name, recipe_url, ingredients])
                writer.writerow([])

        print(f"Recipes saved to recipes.csv")
    else:
        print("No recipes found")


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    save_to_csv(results, ingredient)


if __name__ == "__main__":
    run()