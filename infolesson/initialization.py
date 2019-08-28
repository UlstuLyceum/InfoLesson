from flask import Flask
from infolesson.modules.auth.init import auth

app = Flask(__name__)

app.register_blueprint(auth)
