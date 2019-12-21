import inject
import json
from flask import Blueprint, jsonify, Response, request
from thesheriff.application.gang.request.join_gang_request import \
    JoinGangRequest
from thesheriff.application.outlaw.join_gang import JoinGang
from thesheriff.application.outlaw.create_gang import CreateGang


@inject.autoparams()
def gang_blueprint(join_gang: JoinGang, create_gang: CreateGang) -> Blueprint:
    blueprint_gang = Blueprint('gang', __name__)

    @blueprint_gang.route('/gang/<int:gang_id>/join', methods=['PUT'])
    def join_gang_endpoint(gang_id: int) -> Response:
        data = request.json

        outlaw_id = data.get('outlaw_id')

        join_gang.execute(JoinGangRequest(gang_id, outlaw_id))

        message = {'status': 204, 'message': 'Banda updated'}

        return jsonify(message)

    @blueprint_gang.route('/gang', methods=['POST'])
    def create_gang_endpoint() -> Response:
        data = request.json

        outlaw_id = data.get('owner_id')
        name = data.get('name')

        gang = create_gang.execute(outlaw_id, name)

        gang_json = json.dumps(gang)

        message = {'status': 201, 'gang': gang_json}

        return jsonify(message)

    return blueprint_gang
