import os

from flask import Flask, request
from flask.ext.babel import Babel

from gae.views.home import home_app


babel = Babel()


def create_app(name=None, config=None):
    application_id = os.environ.get('APPLICATION_ID')
    app = Flask(name or application_id)

    app.config.from_object('gae.settings')

    if isinstance(config, dict):
        app.config.update(config)
    elif config:
        app.confg.from_pyfile(os.path.abspath(config))

    babel.init_app(app)
    setup_babel(app)

    app.register_blueprint(home_app)

    return app


def setup_babel(app):

    default = app.config.get('BABEL_DEFAULT_LOCALE', 'en')
    supported = app.config.get('BABEL_SUPPORTED_LOCALES', ['en', 'zh'])

    @babel.localeselector
    def locale_selector():
        return request.accept_languages.best_match(supported, default)
