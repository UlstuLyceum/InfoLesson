from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from flask_security.forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField
from wtforms.validators import InputRequired

try:
    import infolesson.local_config as config
except ImportError:
    import infolesson.example_config as config

from infolesson.modules.auth.auth import auth

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.register_blueprint(auth)

# Flask SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECURITY_PASSWORD_SALT"] = config.SECURITY_SALT
app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = ["username"]
db = SQLAlchemy(app, session_options={"expire_on_commit": False})

# Flask Security
from infolesson.utils.models import User, Role


class ExtendedLoginForm(LoginForm):
    email = StringField("Username", [InputRequired()])


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, login_form=ExtendedLoginForm)


# Index page
@app.route('/')
def index():
    return 'Main page'
