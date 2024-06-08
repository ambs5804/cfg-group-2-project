from flask import Flask, render_template, request, session
from web_environ_config import Config
from converter import convert_units
from recipe_constructor import recipe_constructor
from api_utils import recipe_search
import secrets
import requests

app = Flask(__name__)
# Keep this line to generate a random secret key
app.secret_key = secrets.token_hex(16)

app.config.from_object(Config)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    try:
        ingredients = request.args.get('ingredients')
        mapped_api_data = recipe_search(ingredients)
        formatted_data = recipe_constructor(mapped_api_data)
        return render_template("recipes.html", data=formatted_data)
    except:  # error:
        pass  # similar to "recipe not found"


@app.route('/ingredients')
def ingredients():
    ingredient = request.args.get('ingredients')
    # data = sql_function(ingredient)
    return render_template('ingredients.html', title='Ingredient Substitutions')


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
            result = "Please insert a valid value"
    return render_template('converter.html', title='Converter', result=result)


@app.route('/saves')
def saves():
    pass
    # data = requests.get("http://localhost:3000/")
    # recipe_results = data.json()
    return render_template('saves.html', title='Saved recipes')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
