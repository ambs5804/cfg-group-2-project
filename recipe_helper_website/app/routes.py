from flask import Flask, render_template, request, session
from config import Config
from converter import convert_units
import secrets
import requests
import json

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Keep this line to generate a random secret key
SESSION_TYPE = "filesystem"

app.config.from_object(Config)

# Keep the recipe_search and save_to_json functions as they are
def recipe_search(ingredient):
    # Replace 'ac2be905' and '0809ac9cd1c28ee2e43b387a5c182265' with actual values
    app_id = 'ac2be905'  # Edamam API app ID
    app_key = '0809ac9cd1c28ee2e43b387a5c182265'  # Edamam API app key
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']

def save_to_json(recipes, ingredient):
    # Keep this function as it is
    if recipes:
        file_name = f"{ingredient}_recipes.json"
        recipes_list = []

        for recipe in recipes:
            recipe_info = recipe['recipe']
            recipe_name = recipe_info['label']
            recipe_url = recipe_info['url']
            recipe_image = recipe_info.get('image') #Updated to include image
            ingredients = recipe_info['ingredientLines']
            recipes_list.append({
                'Recipe': recipe_name,
                'URL': recipe_url,
                'Image': recipe_image, # Updated to include image
                'Ingredients': ingredients
            })

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(recipes_list, file, ensure_ascii=False, indent=4)

        print(f"Recipes saved to {file_name}")
    else:
        print("No recipes found")

@app.route('/')
@app.route('/homepage')
def homepage():
    session['test'] = 'hello'
    return render_template('homepage.html', title='Home')

# @app.route('/recipes', methods=['GET', 'POST'])
# def recipes():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect(url_for('homepage'))
#     return render_template('recipes.html', title='Sign In', form=form)

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    ingredients = request.args.get('ingredients')
    print(session['test'])
    # edamame_search_function (ingredients)
    # Call the recipe_search function to fetch recipe data
    recipe_data = recipe_search(ingredients)
    # Save fetched recipe data to JSON
    save_to_json(recipe_data, ingredients)
    # recipe_data = f' these are the searched ingredients {ingredients}'
    return render_template("recipes.html", data=recipe_data)

@app.route('/ingredients')
def ingredients():
    # alternatives = function_for_alternatives()
    alternatives = [(1, 2, 3, 4), (5, 6, 7, 8)]
    return render_template('ingredients.html', title='Ingredient Substitutions', given_ingredient='banana', data=alternatives)

# @app.route('/converter', methods=['GET', 'POST'])
# def converter():
#     return render_template('converter.html', title='converter')

@app.route('/converter', methods=['GET', 'POST'])
def converter():
    result = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = convert_units(amount, from_unit, to_unit)
        except ValueError:
            result = "Please insert a valid amount"
    return render_template('converter.html', title='Converter', result=result)

@app.route('/saves')
def saves():
    data = requests.get("http://localhost:3000/")
    recipe_results = data.json()
    print(recipe_results)
    #return render_template('saves.html', title='Saved recipes')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
