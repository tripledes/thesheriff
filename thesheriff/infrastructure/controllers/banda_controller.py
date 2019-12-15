import inject
import json
from flask import Blueprint, jsonify, Response, request

from thesheriff.application.banda.request.unirse_a_banda_request import UnirseABandaRequest
from thesheriff.application.bandido.unirse_a_banda import UnirseABanda
from thesheriff.application.bandido.crear_banda import CrearBanda


@inject.autoparams()
def banda_blueprint(unirse_a_banda: UnirseABanda, crear_banda: CrearBanda) -> Blueprint:
    blueprint_banda = Blueprint("banda", __name__)

    @blueprint_banda.route("/banda/<int:banda_id>/unirse", methods=['PUT'])
    def unirse_a_banda(banda_id: int) -> Response:
        data = request.json

        bandido_id = data.get('bandido_id')

        unirse_a_banda.execute(UnirseABandaRequest(banda_id, bandido_id))

        message = {'status': 204, 'message': "Banda updated"}

        return jsonify(message)

    @blueprint_banda.route("/banda", methods=['POST'])
    def crear_banda() -> Response:
        data = request.json

        bandido_id = data.get('creador_id')
        nombre = data.get('nombre')

        banda = crear_banda.execute(bandido_id, nombre)

        banda_json = json.dumps(banda)

        message = {'status': 201, 'banda': banda_json}

        return jsonify(message)

    return blueprint_banda
