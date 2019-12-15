import json

import inject
from flask import Blueprint, jsonify, Response, request

from thesheriff.application.bandido.crear_bandido import CrearBandido
from thesheriff.application.bandido.listar_amigos import ListarAmigos
from thesheriff.application.bandido.listar_bandas import ListarBandas
from thesheriff.application.bandido.request.crear_bandido_request import CrearBandidoRequest


@inject.autoparams()
def bandido_blueprint(crear_bandido: CrearBandido,listar_amigos: ListarAmigos, listar_bandas: ListarBandas) -> Blueprint:
    blueprint_bandido = Blueprint("bandio", __name__)

    @blueprint_bandido.route("/bandido/<int:bandido_id>/amigo", methods=['GET'])
    def get_amigos(bandido_id: int) -> Response:
        amigos = listar_amigos.execute(bandido_id)

        amigos_json = json.dumps(amigos)

        message = {'status': 200, 'amigos': amigos_json}

        return jsonify(message)

    @blueprint_bandido.route("/bandido/<int:bandido_id>/banda", methods=['GET'])
    def get_bandas(bandido_id: int) -> Response:
        bandas_del_bandido = listar_bandas.execute(bandido_id)

        bandas_json = json.dumps(bandas_del_bandido)

        message = {'status': 200, 'bandas': bandas_json}

        return jsonify(message)

    @blueprint_bandido.route("/bandido/", methods=['POST'])
    def crear_bandido() -> Response:
        data = request.json

        crear_bandido.execute(CrearBandidoRequest(data.get('nombre'), data.get('correo')))

        message = {'status': 201, 'message': "Bandido added successfully"}

        return jsonify(message)

    return blueprint_bandido
