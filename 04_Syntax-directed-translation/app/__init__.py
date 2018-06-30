import os
from flask import Flask, request, current_app
from ext import bootstrap,babel,Config

def create_app(config_class=Config):
    app = Flask(__name__)
    # app.config['SECRET_KEY']='dai3hoahudhiuahduiah'
    # app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'
    app.config.from_object(config_class)


    bootstrap.init_app(app)
    babel.init_app(app)


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

from app import models
