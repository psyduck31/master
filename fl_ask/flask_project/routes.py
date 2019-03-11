from flask import render_template, url_for, flash, redirect, request
from flask_project import app, db, bcrypt
from flask_project.models import User, Raspisanie
from flask_project.forms import Registration, Login, Edit
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3, json


@app.route('/registration', methods=["GET", "POST"])
def registration():
	if current_user.is_authenticated:
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
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=True)
			return redirect(url_for('home'))
		else:
			flash('Неверно введен логин или пароль, либо пользователь не сущесвует!', 'error')
	return render_template('login.html', form=form)


@app.route('/')
def home():
	conn = sqlite3.connect('flask_project/site.db')
	c = conn.cursor()
	c.execute('SELECT * FROM raspisanie')
	all_rows = c.fetchall()
	return render_template('day.html', all_rows=all_rows)

@app.route('/edit', methods=["GET", "POST"])
@login_required
def edit():
	form = Edit()
	if form.validate_on_submit():
		print(form.data)
		conn = sqlite3.connect('flask_project/site.db')
		c = conn.cursor()
		c.execute("""UPDATE raspisanie SET day_1 = ?, day_2 = ?, day_3 = ?, day_4 = ?, day_5 = ?, day_6 = ? WHERE day = ?""",
			(form.day_1.data, form.day_2.data, form.day_3.data, form.day_4.data, form.day_5.data, form.day_6.data, form.day.data))
		conn.commit()
	return render_template('edit.html', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/api/raspisanie/all', methods=["GET"])
def api_raspisanie():
	conn = sqlite3.connect('flask_project/site.db')
	c = conn.cursor()
	c.execute("SELECT * FROM raspisanie")
	rot = c.fetchall()
	return json.dumps(rot, ensure_ascii=False)


@app.route('/api/raspisanie', methods=["GET"])
def api_id():
	conn = sqlite3.connect('flask_project/site.db')
	c = conn.cursor()
	c.execute("SELECT * FROM raspisanie")
	all = c.fetchall()
	if 'id' in request.args:
		id = int(request.args['id'])
	if 0 <= id <= 4:
		return json.dumps(all[id], ensure_ascii=False)
	else:
		return 'Нет такого айди'
@app.route('/api/raspisanie/edit', methods=["POST"])
def api_edit():
	conn = sqlite3.connect('flask_project/site.db')
	c = conn.cursor()
	if request.method == 'POST':
		day = str(request.args['day'])
		day_1 = str(request.args['day_1'])
		day_2 = str(request.args['day_2'])
		day_3 = str(request.args['day_3'])
		day_4 = str(request.args['day_4'])
		day_5 = str(request.args['day_5'])
		day_6 = str(request.args['day_6'])
		c.execute("""UPDATE raspisanie SET day_1 = ?, day_2 = ?, day_3 = ?, day_4 = ?, day_5 = ?, day_6 = ? WHERE day = ?""",
			(day_1, day_2, day_3, day_4, day_5, day_6, day))
		conn.commit()
	return 'api post request'