from flask import render_template, url_for, flash, redirect, request
from flask_project import app, db, bcrypt
from flask_project.models import User
from flask_project.forms import Registration, Login
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
	return('Hello world!')


@app.route('/registration', methods=["GET", "POST"])
def registration():
	if current_user.is_authenticated():
		return redirect(url_for('home'))
	form = Registration()
	if form.validate_on_submit():
		username = User.query.filter_by(username=form.username.data).first()
		email = User.query.filter_by(email=form.email.data).first()
		if username or email:
			flash('Аккаунт с данным логином или email уже был зарегистрирован.', 'error')
		else:
			hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			new_user = User(username=form.username.data, email=form.email.data, password=hash_password)
			db.session.add(new_user)
			db.session.commit()
			flash('Благодарим за регистрацию, ' + form.username.data + '!', 'success')
	return render_template('registration.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=True)
			return redirect(url_for('home'))
	return render_template('login.html', form=form)


@app.route('/check')
@login_required
def check():
	return('Вы успешно вошли в аккаунт')


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))