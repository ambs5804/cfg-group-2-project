from flask import Flask, render_template, flash, redirect, url_for, session, request
# pip install Flask-ession
# flash() function is a useful way to show a message to the user.
# redirect(). This function instructs the client web browser to automatically navigate to a different page, given as an argument
from config import Config
from forms import LoginForm

app = Flask(__name__)
SESSION_TYPE = "filesystem"


app.config.from_object(Config)
# app.config.from_object(Config, __name__)
# Session(app)


@app.route('/')
@app.route('/homepage')
# def set_session():
#     ""
#     # flask sessions
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
    # edamame_search_functiion (ingredients)
    recipe_data = f' these are the searched ingredients {ingredients}'
    return render_template("recipes.html", data=recipe_data)


@app.route('/ingredients')
def ingredients():
    # alternatives = function_for_alternatives()
    alternatives = [(1, 2, 3, 4), (5, 6, 7, 8)]
    return render_template('ingredients.html', title='Ingredient Substitutions', given_ingredient='banana', data=alternatives)


@app.route('/converter', method=['GET', 'POST'])
def converter():

    return render_template('converter.html', title='converter')


@app.route('/saves')
def saves():
    return render_template('saves.html', title='Saved recipes')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
