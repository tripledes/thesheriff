from flask import Flask

from thesheriff.configuration import configure_inject, configure_application
from thesheriff.infrastructure.asalto.asalto_controller import asalto_blueprint


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(
        asalto_blueprint(), url_prefix="/api/v1")

    return application
