from flask import Flask
from flask_login import current_user
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

from infolesson.modules.auth.forms import *
from infolesson.utils.basic_utils import render

try:
    import infolesson.local_config as config
except ImportError:
    import infolesson.example_config as config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# Flask SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECURITY_PASSWORD_SALT"] = config.SECURITY_SALT
app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = ["username"]

# Flask Security Templates
db = SQLAlchemy(app, session_options={"expire_on_commit": False})

# Flask Security
app.config["SECURITY_REGISTERABLE"] = True
from infolesson.utils.models import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, login_form=ExtendedLoginForm)


# Index page
@app.route("/")
def index():
    return render("index.html", current_user=current_user)


# Register blueprints
from infolesson.modules.auth.auth import auth
from infolesson.modules.classes.classes import classes

app.register_blueprint(auth)
app.register_blueprint(classes)
