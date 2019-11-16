from flask import Flask, json
from logging.config import dictConfig


def create_app():
    """ Create and return the application object """
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_pyfile('config.py')

    @app.route("/", methods=["GET"])
    def index():
        return json.jsonify("Welcome to The Sheriff!")
    
    return app