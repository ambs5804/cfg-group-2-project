from db_utils import find_substitution


@app.route('/ingredients')
def ingredients():
    sub_ingredient = request.args.get('ingredients')
    substitutes = find_substitution(sub_ingredient)
    return render_template('ingredients.html', title='Ingredient Substitutions', substitutes=substitutes)
