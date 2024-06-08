from config import API_KEY, API_ID
import requests

# Reformat by Simone
# Reformat of Ruth's original code for API call functions, so that it can correctly work in routes.py
# change: no longer saving to json, just mapping parsed data from API function, no longer printing to terminal

# json_data_mappper previously called saved_to_json- now just mapping data, no longer saving to json


def json_data_mapper(recipes):
    recipes_list = []

    for recipe in recipes:
        recipe_info = recipe['recipe']
        recipe_name = recipe_info['label']
        recipe_url = recipe_info['url']
        recipe_image = recipe_info.get('image')  # Updated to include image
        ingredients = recipe_info['ingredientLines']
        recipes_list.append({
            'Recipe': recipe_name,
            'URL': recipe_url,
            'Image': recipe_image,  # Updated to include image
            'Ingredients': ingredients
        })
    return recipes_list


def recipe_search(ingredient):
    # Replace 'ac2be905' and '0809ac9cd1c28ee2e43b387a5c182265' with actual values
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(
            ingredient, API_ID, API_KEY)
    )
    data = result.json()
    return json_data_mapper(data['hits'])
