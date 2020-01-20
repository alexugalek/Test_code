from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Alex'}
	
	posts = [
		{
			'author': {'username': 'Misha'},
			'body': 'My name is Misha'
		},
		{
			'author': {'username': 'Nastya'},
			'body': 'My name is Nastya'
		},
		{  	'author': {'username': 'Tana'},
			'body': 'My name is Tana'
		}
		]

	return render_template('index.html', user=user, title='Title', posts=posts)

@app.route('/secondpage')
def second_page():
	return render_template('secondpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login requested for user {form.username.data}, {form.remember_me.data}')
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)