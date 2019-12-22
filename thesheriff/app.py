from flask import Flask

from thesheriff.configuration import configure_inject, configure_application
from thesheriff.infrastructure.controllers.raid_controller import \
    raid_controller
from thesheriff.infrastructure.controllers.outlaw_controller import \
    outlaw_controller
from thesheriff.infrastructure.controllers.gang_controller import \
    gang_controller


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(raid_controller(), url_prefix="/api/v1")
    application.register_blueprint(outlaw_controller(), url_prefix="/api/v1")
    application.register_blueprint(gang_controller(), url_prefix="/api/v1")

    return application
