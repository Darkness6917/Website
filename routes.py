from app import app
from flask import render_template, url_for
from forms import Registration, Login
from flask import flash, redirect
app.config['SECRET_KEY'] = '124hjok83241f924f293d123dgs3'
posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Jane'},
        'body': 'Beautiful day in Portland!'   
    }
]
username = {'username': 'Miguel'}
#sets the URL to the def function and will display when connection is made to the "/XXXX" 
@app.route('/')
@app.route('/index')
#defines index to be used on the @app.route above
def index():
    return render_template('index.html', title = 'Home', post = posts, user = username)
@app.route('/about')
def about():
    return render_template('about.html',)
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('index'))
    return render_template('register.html', title = 'Register', form=form)
@app.route('/login')
def login():
    form = Login()
    return render_template('login.html', title = 'Login', form=form)