from flask import Flask

from thesheriff.configuration import configure_inject, configure_application
from thesheriff.infrastructure.controllers.raid_controller import \
    raid_blueprint
from thesheriff.infrastructure.controllers.outlaw_controller import \
    outlaw_blueprint
from thesheriff.infrastructure.controllers.gang_controller import \
    gang_blueprint


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(raid_blueprint(), url_prefix="/api/v1")
    application.register_blueprint(outlaw_blueprint(), url_prefix="/api/v1")
    application.register_blueprint(gang_blueprint(), url_prefix="/api/v1")

    return application
