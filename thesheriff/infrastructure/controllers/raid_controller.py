import inject
from flask import Blueprint, jsonify, Response, request
from thesheriff.domain.outlaw.outlaw import Outlaw
#from thesheriff.application.bandido.crear_asalto import CrearAsalto
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.domain.outlaw.score import Score


@inject.autoparams()
def raid_blueprint(rate_raid: RateRaid) -> Blueprint:
    # def asalto_blueprint(
    #        crear_asalto: CrearAsalto, puntuar_asalto: PuntuarAsalto) -> Blueprint:
    """Create routes for entity Asalto

    :param crear_asalto: Object with asalto creation implementation.
    :param puntuar_asalto: Object with asalto rating implementation.
    :returns: Blueprint
    """
    blueprint_raid = Blueprint('raid', __name__)

 #   @asalto_blueprint.route("/asalto", methods=['POST'])
 #   def create_asalto() -> Response:
 #       """create_asalto registers an Asalto
 #       :return: Response.
 #       """
 #       #FIXME(tripledes)
 #       # CrearAsalto is still not implemented, this code will need to adapt
 #       # to its signature (we'll probably require bandido ID)
 #       new_asalto = request.json
 #       asalto = crear_asalto.execute(**new_asalto)
 #       return jsonify(asalto.to_dict())

    @blueprint_raid.route("/raid/<int:asalto_id>/rate", methods=['POST'])
    def rate_raid_endpoint(raid_id: int) -> Response:
        """rate_raid_endpoint recives rates for a Raid an executes
           the Rate Raid use case.
        :param raid_id: Id of the Asalto to be rated
        :type raid_id: Integer.
        :returns: Response -- Flask Response.
        """
        data = request.json
        outlaw_id = data.get('outlaw_id')
        rate = data.get('rate')
        score = Score(**rate)
        rate_raid.execute(outlaw_id, score)
        message = {'raid_id': raid_id, 'message': 'rated successfully'}
        return jsonify(message)

    return blueprint_raid
