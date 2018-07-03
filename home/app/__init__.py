from flask import Flask
from flask_bootstrap import Bootstrap
from flask_babel import _, Babel
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
bootstrap = Bootstrap()
babel = Babel()
bootstrap.init_app(app)
babel.init_app(app)

from app import routes