import requests
import json

def recipe_search(ingredient):
    app_id = 'ac2be905'  # Edamam API app ID
    app_key = '0809ac9cd1c28ee2e43b387a5c182265'  # Edamam API app key
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']

def save_to_json(recipes, ingredient):
    if recipes:
        file_name = f"{ingredient}_recipes.json"
        recipes_list = []

        for recipe in recipes:
            recipe_info = recipe['recipe']
            recipe_name = recipe_info['label']
            recipe_url = recipe_info['url']
            ingredients = recipe_info['ingredientLines']
            recipes_list.append({
                'Recipe': recipe_name,
                'URL': recipe_url,
                'Ingredients': ingredients
            })

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(recipes_list, file, ensure_ascii=False, indent=4)

        print(f"Recipes saved to {file_name}")
    else:
        print("No recipes found")

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    save_to_json(results, ingredient)

if __name__ == "__main__":
    run()
