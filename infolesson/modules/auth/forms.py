from flask_security import LoginForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class ExtendedLoginForm(LoginForm):

    email = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")

