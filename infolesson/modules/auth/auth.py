from flask import Blueprint
from flask_security import current_user

from infolesson.initialization import security
from infolesson.initialization import app

auth = Blueprint("auth", __name__, template_folder="templates")


# Flask Security Messages
app.config["SECURITY_MSG_USER_DOES_NOT_EXIST"] = ("Пользователь с таким логином не существует", 0)
app.config["SECURITY_MSG_INVALID_PASSWORD"] = ("Неверный пароль", 0)


@security.login_context_processor
def security_login_processor():
    return dict(current_user=current_user)

