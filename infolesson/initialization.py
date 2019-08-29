from flask import Flask
from infolesson.modules.auth.init import auth

try:
    import infolesson.local_config as config
except ImportError:
    import infolesson.example_config as config

app = Flask(__name__)

app.register_blueprint(auth)

app.config["CSRF_ENABLED"] = config.CSRF_ENABLED
app.config["SECRET_KEY"] = config.SECRET_KEY


@app.route('/')
def index_page():
    return 'index page'
