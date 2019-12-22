"""
thesheriff.infrastructure.controllers.raid_controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RESTful part of the Raid use cases.
"""
import inject
from flask import Blueprint, jsonify, Response, request
from thesheriff.domain.outlaw.outlaw import Outlaw
# from thesheriff.application.bandido.crear_asalto import CrearAsalto
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.domain.outlaw.score import Score


@inject.autoparams()
def raid_controller(rate_raid: RateRaid) -> Blueprint:
    """raid_controller holds the blueprint for all raid routes.

    :param rate_raid: RateRaid use case implementation.
    :type rate_raid: RateRaid
    :return: Flask Blueprint.
    :rtype: Blueprint

    Implements the following routes:

    """
    # def asalto_blueprint(
    # crear_asalto: CrearAsalto, puntuar_asalto: PuntuarAsalto) -> Blueprint:
    # """Create routes for entity Raid
    # :param create_raid: Object with raid creation implementation.
    # :param rate_raid: Object with raid rating implementation.
    # :return: The Raid Blueprint.
    # :rtype: Blueprint.
    # """
    blueprint_raid = Blueprint('raid', __name__)

    # @asalto_blueprint.route("/asalto", methods=['POST'])
    # def create_asalto() -> Response:
    #     """create_asalto registers an Asalto
    #     :return: Response.
    #     """
    #     #FIXME(tripledes)
    #     # CrearAsalto is still not implemented, this code will need to adapt
    #     # to its signature (we'll probably require bandido ID)
    #     new_asalto = request.json
    #     asalto = crear_asalto.execute(**new_asalto)
    #     return jsonify(asalto.to_dict())

    return blueprint_raid
