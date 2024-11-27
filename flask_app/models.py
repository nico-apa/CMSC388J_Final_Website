from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField

# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None

# TODO: implement fields
class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True, min_length=1, max_length=40)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    profile_pic = db.ImageField(required=False)

    # Returns unique string identifying our object
    def get_id(self):
        return str(self.id)


# TODO: implement fieldsx
class Review(db.Document):
    commenter = db.ReferenceField(User, required=True)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)
    imdb_id = db.StringField(required=True, min_length=9, max_length=9)
    movie_title = db.StringField(required=True, min_length=1, max_length=100)
    image = db.ImageField()
    #Uncomment when other fields are ready for review pictures