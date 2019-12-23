import inject
import json
from flask import Blueprint, jsonify, Response, request
from thesheriff.application.gang.request.join_gang_request import \
    JoinGangRequest
from thesheriff.application.outlaw.join_gang import JoinGang
from thesheriff.application.outlaw.create_gang import CreateGang
from thesheriff.application.gang.list_gangs import ListGangs


@inject.autoparams()
def gang_controller(
    join_gang: JoinGang, create_gang: CreateGang, list_gangs: ListGangs
) -> Blueprint:
    """gang_controller holds the blueprint for all gang routes.

    :param join_gang: Join Gang use case implementation.
    :type join_gang: JoinGang
    :param create_gang: Create Gang use case implementation.
    :type create_gang: CreateGang
    :param list_gangs: List Gangs use case implementation.
    :type list_gangs: ListGangs
    :return: Flask Blueprint.
    :rtype: Blueprint

    Implements the following routes:

    * */<prefix>/gang* (POST)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/gang \\
             -X POST --data @examples/json/create_gang.json \\
             -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "status": 201,
             "gang": {}
         }
    * */<prefix>/gang/<int:gang_id>/join* (PUT)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/gang/1/join \\
            -X PUT --data @examples/json/join_gang.json \\
            -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "status": 204,
             "message": "Gang updated"
         }
    * */<prefix>/gang* (GET)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/gang

      **Response Example:**

      .. code-block:: json

         {
             "status": 201,
             "gangs": {
                 "gang1": {},
                 "gang2": {}
             }
         }
    """

    blueprint_gang = Blueprint('gang', __name__)

    @blueprint_gang.route('/gang/<int:gang_id>/join', methods=['PUT'])
    def join_gang_endpoint(gang_id: int) -> Response:
        data = request.json

        outlaw_id = data.get('outlaw_id')

        join_gang.execute(JoinGangRequest(gang_id, outlaw_id))

        message = {'status': 204, 'message': 'Gang updated'}

        return jsonify(message)

    @blueprint_gang.route('/gang', methods=['GET', 'POST'])
    def create_gang_endpoint() -> Response:
        if request.method == 'GET':
            gangs = list_gangs.execute()
            message = {'status': 201, 'gangs': gangs}
            return jsonify(message)

        data = request.json

        outlaw_id = data.get('owner_id')
        name = data.get('name')

        gang = create_gang.execute(outlaw_id, name)

        gang_json = json.dumps(gang)

        message = {'status': 201, 'gang': gang_json}

        return jsonify(message)

    return blueprint_gang
