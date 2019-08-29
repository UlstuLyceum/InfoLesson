from flask import session
from infolesson.utils import models


def get_current_user():
    if "login" not in session or "password" not in session:
        return None
    return models.User.find_one({"login": session["login"], "password": session["password"]})
