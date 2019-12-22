import inject
from flask import Blueprint, jsonify, Response, request
from thesheriff.domain.outlaw.outlaw import Outlaw
# from thesheriff.application.bandido.crear_asalto import CrearAsalto
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.domain.outlaw.score import Score


@inject.autoparams()
def raid_blueprint(rate_raid: RateRaid) -> Blueprint:
    # def asalto_blueprint(
    # crear_asalto: CrearAsalto, puntuar_asalto: PuntuarAsalto) -> Blueprint:
    """Create routes for entity Asalto
    :param crear_asalto: Object with asalto creation implementation.
    :param puntuar_asalto: Object with asalto rating implementation.
    :returns: Blueprint
    """
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
