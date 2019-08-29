from flask import Blueprint

from infolesson.utils.perms_control import login_required

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login_page():
    return 'login_page'


@auth.route('/logout')
def logout_page():
    pass


@auth.route('/profile')
@login_required
def profile_page():
    return 'profile page'
