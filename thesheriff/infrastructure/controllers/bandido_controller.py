import inject
from flask import Blueprint, jsonify, Response
from thesheriff.application.bandido.listar_amigos import ListarAmigos
class BandidoController:
    @inject.autoparams()
    def listar_amigos_blueprint(listar_amigos: ListarAmigos) -> Blueprint:
       """Create routes for entity Bandido
        :param listar_amigos: Object with listar_amigos implementation.
        :returns: Blueprint
        """
        listar_amigos_blueprint = Blueprint("listar_amigos", __name__)

    @listar_amigos.route("/bandido/listar_amigos/<int:bandido_id>", methods=['GET'])
    def listar_amigos(bandido_id: int) -> Response:
        """listar_amigos receives the bandido_id that is wanted to print his friends
        :param asalto_id: Id of the bandido
        :type asalto_id: int.
        :return: Response.
        """
        listar_amigos.execute(bandido_id)
        message = {''} #To be filled
        return jsonify(message)

    return listar_amigos_blueprint