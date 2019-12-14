import inject
import json
from flask import Blueprint, jsonify, Response
from thesheriff.application.bandido.listar_amigos import ListarAmigos
from thesheriff.application.bandido.listar_bandas import ListarBandas


@inject.autoparams()
def bandido_blueprint(listar_amigos: ListarAmigos, listar_bandas: ListarBandas) -> Blueprint:
    blueprint_bandido = Blueprint("bandio", __name__)

    @blueprint_bandido.route("/bandido/<int:bandido_id>/amigos", methods=['GET'])
    def get_amigos(bandido_id: int) -> Response:
        amigos = listar_amigos.execute(bandido_id)

        amigos_json = json.dump(amigos)

        message = {'status': 200, 'amigos': amigos_json}

        return jsonify(message)

    @blueprint_bandido.route("/bandido/<int:bandido_id>/banda, methods=['GET']")
    def get_bandas(bandido_id: int) -> Response:
        bandas_del_bandido = listar_bandas.execute(bandido_id)

        bandas_json = json.dump(bandas_del_bandido)

        message = {'status': 200, 'bandas': bandas_json}

        return jsonify(message)

    return blueprint_bandido
