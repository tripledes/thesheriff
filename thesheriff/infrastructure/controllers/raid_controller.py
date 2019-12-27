"""
thesheriff.infrastructure.controllers.raid_controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RESTful part of the Raid use cases.
"""
import inject
from flask import Blueprint, Response, request, jsonify
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.application.raid.create_raid import CreateRaid
from thesheriff.application.raid.request.create_raid_request import \
    CreateRaidRequest
from thesheriff.domain.outlaw.score import Score


@inject.autoparams()
def raid_controller(create_raid: CreateRaid, rate_raid: RateRaid) -> Blueprint:
    """raid_controller holds the blueprint for all raid routes.

    :param create_raid: CreateRaid use case implementation.
    :param rate_raid: RateRaid use case implementation.
    :type create_raid: CreateRaid
    :type rate_raid: RateRaid
    :return: Flask Blueprint.
    :rtype: Blueprint

    Implements the following routes:

    * */<prefix>/raid/* (POST)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/raid/ \\
            -X POST --data @examples/json/create_raid.json \\
            -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "Raid created successfully",
             "raid": {}
         }

    * */<prefix>/outlaw/<int:outlaw_id>/raid/<int:raid_id>/* (PUT)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/raid/1 \\
             -X PUT --data @examples/json/rate_raid.json \\
             -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "Raid rated successfully"
         }
    """
    blueprint_raid = Blueprint('raid', __name__)

    @blueprint_raid.route("/raid", methods=['POST'])
    def create_raid_endpoint() -> Response:
        data = request.get_json()
        new_raid = data.get('raid')
        raid_request = CreateRaidRequest(new_raid.get('name'),
                                         new_raid.get('date'),
                                         new_raid.get('location'),
                                         new_raid.get('gang_id'),
                                         new_raid.get('sheriff_id'),
                                         new_raid.get('outlaw_ids'))

        raid = create_raid.execute(raid_request)

        message = {
            'message': 'Raid created successfully',
            'raid': {'id': raid.id, 'name': raid.name}
        }
        return jsonify(message)

    @blueprint_raid.route("/raid/<int:raid_id>/rate",
                          methods=['PUT'])
    def rate_raid_endpoint(raid_id: int) -> Response:
        """rate_raid_endpoint recives rates for a Raid an executes
           the Rate Raid use case.

        :param raid_id: Id of the Raid to be rated
        :type raid_id: Integer
        :return: Flask Response.
        :rtype: Response
        """
        data = request.json
        outlaw_id = data.get('outlaw_id')
        rate = data.get('rate')
        score = Score(**rate)
        rate_raid.execute(outlaw_id, raid_id, score)

        message = {'message': 'Raid rated successfully'}

        return jsonify(message)

    return blueprint_raid
