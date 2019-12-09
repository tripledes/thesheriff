"""
.. module:: asalto_controller
   :platform: Windows,Unix
   :synopsis: Asalto RESTful controller
.. moduleauthor:: The Sheriff Team <thesheriff@team.net>
"""
import inject

from flask import Blueprint, jsonify, Response, request
from thesheriff.domain.asalto import Asalto
from thesheriff.application.bandido.crear_asalto import CrearAsalto
from thesheriff.application.bandido.puntuar_asalto import PuntuarAsalto
from thesheriff.domain.bandido.puntuacion import Puntuacion


@inject.autoparams()
def asalto_blueprint(
        crear_asalto: CrearAsalto, puntuar_asalto: PuntuarAsalto) -> Blueprint:
    """Create routes for entity Asalto

    :param crear_asalto: Object with asalto creation implementation.
    :param puntuar_asalto: Object with asalto rating implementation.
    :returns: Blueprint
    """
    asalto_blueprint = Blueprint("asalto", __name__)

    @asalto_blueprint.route("/asalto", methods=['POST'])
    def create_asalto() -> Response:
        """create_asalto registers an Asalto
        :return: Response.
        """
        #FIXME(tripledes)
        # CrearAsalto is still not implemented, this code will need to adapt
        # to its signature (we'll probably require bandido ID)
        new_asalto = request.json
        asalto = crear_asalto.execute(**new_asalto)
        return jsonify(asalto.to_dict())

    @asalto_blueprint.route("/asalto/rate/<int:asalto_id>", method=['POST'])
    def rate_asalto(asalto_id: int) -> Response:
        """rate_asalto recives rates for an asalto an executes
           the Puntuar Asalto use case.
        :param asalto_id: Id of the Asalto to be rated
        :type asalto_id: int.
        :return: Response.
        """
        data = request.json
        bandido_id = data.get('bandido_id')
        rating = data.get('rating')
        score = Puntuacion(**rating)
        puntuar_asalto.execute(bandido_id, score)
        message = {'asalto_id': asalto_id, 'message': 'rated successfully'}
        return jsonify(message)

    return asalto_blueprint
