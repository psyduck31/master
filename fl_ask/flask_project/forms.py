from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Registration(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Зарегистрироваться')


class Login(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class Edit(FlaskForm):
	day = SelectField('День недели', choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), 
		('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница')], validators=[DataRequired()])
	day_1 = StringField('Первая пара')
	day_2 = StringField('Вторая пара')
	day_3 = StringField('Третья пара')
	day_4 = StringField('Четвертая пара')
	day_5 = StringField('Пятая пара')
	day_6 = StringField('Шестая пара')
	submit = SubmitField('Изменить расписание')


class Edit_api(FlaskForm):
	day = StringField(validators=[DataRequired()])
	day_1 = StringField()
	day_2 = StringField()
	day_3 = StringField()
	day_4 = StringField()
	day_5 = StringField()
	day_6 = StringField()