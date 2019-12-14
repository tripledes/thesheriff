from flask import Flask

from thesheriff.configuration import configure_inject, configure_application
from thesheriff.infrastructure.controllers.asalto_controller import asalto_blueprint
from thesheriff.infrastructure.controllers.bandido_controller import bandido_blueprint


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(asalto_blueprint(), url_prefix="/api/v1")
    application.register_blueprint(bandido_blueprint(), url_prefix="/api/v1")

    return application
