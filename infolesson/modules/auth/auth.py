from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login')
def login_page():
    return render_template('login.html')
