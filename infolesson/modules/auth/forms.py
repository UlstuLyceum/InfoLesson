from flask_security import LoginForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class ExtendedLoginForm(LoginForm):

    email = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")
