from flask_project import db
from flask_project.models import User
print(User.query.all())