import os
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
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

    # Ejemplo de como conectar a DB y crear un primer módelo
    db_host = os.environ.get('DB_HOST', None)
    db_name = os.environ.get('DB_NAME', None)
    db_user = os.environ.get('DB_USER', None)
    db_pass = os.environ.get('DB_PASSWD', None)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
        db_user + ':' + db_pass + '@' + db_host + '/' + db_name

    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    db.create_all()
    guest = User(username='guest', email='guest@example.com')
    # Fin ejemplo

    @app.route("/", methods=["GET"])
    def index():
        return json.jsonify(user=guest.username, email=guest.email)

    return app
