from flask_project import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.id}')"


class Raspisanie(db.Model):
    day = db.Column(db.String(255), primary_key=True)
    day_1 = db.Column(db.String(255), nullable=True)
    day_2 = db.Column(db.String(255), nullable=True)
    day_3 = db.Column(db.String(255), nullable=True)
    day_4 = db.Column(db.String(255), nullable=True)
    day_5 = db.Column(db.String(255), nullable=True)
    day_6 = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Schedule('{self.day}', '{self.day_1}', '{self.day_2}', '{self.day_3}', '{self.day_4}', '{self.day_5}'," \
            f" '{self.day_6}', )"
