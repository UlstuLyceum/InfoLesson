from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
