from flask import Blueprint
from flask_security import current_user, login_required, roles_accepted

from infolesson.utils.basic_utils import render

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login2")  # TODO remove
@roles_accepted("admin")
def login_page():
    return render("login.html")
