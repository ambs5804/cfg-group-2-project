from flask import Flask, render_template, flash, redirect, url_for
# flash() function is a useful way to show a message to the user.
# redirect(). This function instructs the client web browser to automatically navigate to a different page, given as an argument
from config import Config
from forms import LoginForm

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
@app.route('/homepage')
def homepage():
    user = {'username': 'Group 2'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('homepage.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('homepage'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
