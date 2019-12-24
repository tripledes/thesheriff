"""
thesheriff.infrastructure.controllers.raid_controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RESTful part of the Raid use cases.
"""
import json

import inject
from flask import Blueprint, Response, request, make_response

from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.application.raid.create_raid import CreateRaid
from thesheriff.application.raid.create_raid_request import CreateRaidRequest
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
             "status": 201,
             "message": "Raid added successfully"
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
             "status": 204,
             "message": "raid rated successfully"
         }
    """
    blueprint_raid = Blueprint('raid', __name__)

    @blueprint_raid.route("/raid", methods=['POST'])
    def create_raid() -> Response:
        #     """create_raid registers a Raid
        #     :return: Response.
        #     """
        data = request.get_json()
        new_raid = data.get('raid')
        raid_request = CreateRaidRequest(new_raid.get('name'),
                                         new_raid.get('date'),
                                         new_raid.get('location'),
                                         new_raid.get('gang_id'),
                                         new_raid.get('sheriff_id'),
                                         new_raid.get('outlaw_ids'))

        raid = create_raid.execute(raid_request)

        raid_json = json.dumps(raid.__dict__)
        resp = make_response(raid_json, 201)
        return resp

    @blueprint_raid.route("/outlaw/<int:outlaw_id>/raid/<int:raid_id>/",
                          methods=['PUT'])
    def rate_raid(outlaw_id: int, raid_id: int) -> Response:
        """rate_raid recives rates for a Raid an executes
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
        message = {'message': 'rated successfully'}
        return make_response(message, 204)

    return blueprint_raid
