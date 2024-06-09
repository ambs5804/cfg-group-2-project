from flask import Flask, render_template, request
from web_environ_config import Config
from converter import convert_units
from recipe_constructor import recipe_constructor, make_it_dict
from api_utils import recipe_search
import secrets
from db_utils import find_substitution


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
        saveable_data = make_it_dict(formatted_data)
        return render_template("recipes.html", data=formatted_data, recipe_data=saveable_data, title='Recipes')
    except Exception as e:
        print(e)
        print("no")


@app.route('/ingredients')
def ingredients():
    sub_ingredient = request.args.get('ingredients')
    substitutes = find_substitution(sub_ingredient)
    return render_template('ingredients.html', title='Ingredient Substitutions', substitutes=substitutes)


@ app.route('/converter', methods=['GET', 'POST'])
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


@ app.route('/recipe/<id>')
def recipe(id):

    return render_template('recipe.html', id=id, title='Recipe')


@ app.route('/saves')
def saves():
    pass
    # This feature is not implemented yet, but it will be in the future
    return render_template('saves.html', title='Saved recipes')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
