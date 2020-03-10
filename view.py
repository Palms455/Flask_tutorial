from app import app
from flask import render_template
from forms import LoginForm

@app.route('/')
def index():
	
	return render_template('web/index.html', )


@app.route('/account')
def login():
    form = LoginForm()
    return render_template('web/account.html', title='Sign In', form=form)