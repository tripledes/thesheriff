"""
thesheriff.infrastructure.controllers.outlaw_controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RESTful part of the Outlaw use cases.

"""
import json
import inject
from flask import Blueprint, jsonify, Response, request
from thesheriff.application.outlaw.create_outlaw import CreateOutlaw
from thesheriff.application.outlaw.list_friends import ListFriends
from thesheriff.application.outlaw.list_gangs import ListGangs
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.application.outlaw.request.create_outlaw_request import \
    CreateOutlawRequest
from thesheriff.domain.outlaw.score import Score


@inject.autoparams()
def outlaw_controller(
        create_outlaw: CreateOutlaw, list_friends: ListFriends,
        list_gangs: ListGangs
) -> Blueprint:
    """outlaw_controller holds the blueprint for all outlaw routes.

    :param create_outlaw: Create Outlaw use case implementation.
    :type create_outlaw: CreateOutlaw
    :param list_friends: List Friends use case implementation.
    :type list_friends: ListFriends
    :param list_gangs: List Gangs use case implementation.
    :type list_gangs: ListGangs
    :return: Flask Blueprint.
    :rtype: Blueprint

    Implements the following routes:

    * */<prefix>/outlaw/* (POST)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/ \\
            -X POST --data @examples/json/create_outlaw.json \\
            -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "Outlaw added successfully",
             "status": 201
         }

    * */<prefix>/outlaw/<int:outlaw_id>/friends* (GET)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/friends

      **Response Example:**

      .. code-block:: json

         {
             "status": 200,
             "friends": {
                 "friend1": {},
                 "friend2": {}
             }
         }
    * */<prefix>/outlaw/<int:outlaw_id>/gangs* (GET)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/gangs

      **Response Example:**

      .. code-block:: json

         {
             "status": 200,
             "gangs": {
                 "gang1": {},
                 "gang2": {}
             }
         }
    * */<prefix>/outlaw/<int:outlaw_id>/raid/<int:raid_id>/* (POST)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/raid/1 \\
             -X POST --data @examples/json/rate_raid.json \\
             -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "status": 201,
             "message": "raid rated successfully"
         }
    """
    blueprint_outlaw = Blueprint('outlaw', __name__)

    @blueprint_outlaw.route('/outlaw/<int:outlaw_id>/friends', methods=['GET'])
    def get_friends_endpoint(outlaw_id: int) -> Response:
        friends = list_friends.execute(outlaw_id)

        friends_json = json.dumps(friends)

        message = {'status': 200, 'friends': friends_json}

        return jsonify(message)

    @blueprint_outlaw.route('/outlaw/<int:outlaw_id>/gangs', methods=['GET'])
    def get_gangs_endpoint(outlaw_id: int) -> Response:
        outlaw_gangs = list_gangs.execute(outlaw_id)

        gangs_json = json.dumps(outlaw_gangs)

        message = {'status': 200, 'gangs': gangs_json}

        return jsonify(message)

    @blueprint_outlaw.route('/outlaw/', methods=['POST'])
    def create_outlaw_endpoint() -> Response:
        data = request.get_json()
        # TODO(all): if outlaw is None we should return an HTTP error
        new_outlaw = data.get('outlaw')

        create_outlaw.execute(CreateOutlawRequest(
            new_outlaw.get('name'), new_outlaw.get('email')))

        message = {'status': 201, 'message': 'Outlaw added successfully'}

        return jsonify(message)

    @blueprint_outlaw.route("/outlaw/<int:outlaw_id>/raid/<int:raid_id>/",
                            methods=['PUT'])
    def rate_raid_endpoint(outlaw_id: int, raid_id: int) -> Response:
        """rate_raid_endpoint recives rates for a Raid an executes
           the Rate Raid use case.
        :param raid_id: Id of the Raid to be rated
        :type raid_id: Integer.
        :param outlaw_id: Id of the Outlaw performing the rata
        :type outlaw_id: Integer.
        :returns: Response -- Flask Response.
        """
        data = request.json
        rate = data.get('rate')
        score = Score(**rate)
        rate_raid.execute(outlaw_id, raid_id, score)
        message = {'status': 201, 'message': 'rated successfully'}
        return jsonify(message)

    return blueprint_outlaw
