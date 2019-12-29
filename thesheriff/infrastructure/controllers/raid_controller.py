"""
thesheriff.infrastructure.controllers.raid_controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RESTful part of the Raid use cases.
"""
import inject
from flask import Blueprint, Response, request, jsonify
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.application.raid.create_raid import CreateRaid
from thesheriff.application.raid.end_raid import EndRaid
from thesheriff.application.raid.grade_raid import GradeRaid
from thesheriff.application.raid.request.create_raid_request import \
    CreateRaidRequest
from thesheriff.application.raid.request.end_raid_request import EndRaidRequest
from thesheriff.application.raid.request.grade_raid_request import \
    GradeRaidRequest
from thesheriff.application.raid.request.rate_raid_request import \
    RateRaidRequest
from thesheriff.domain.outlaw.score import Score


@inject.autoparams()
def raid_controller(create_raid: CreateRaid, rate_raid: RateRaid,
                    grade_raid: GradeRaid, end_raid: EndRaid) -> Blueprint:
    """raid_controller holds the blueprint for all raid routes.

    :param create_raid: CreateRaid use case implementation.
    :param rate_raid: RateRaid use case implementation.
    :param grade_raid: GradeRaid use case implementation.
    :param end_raid: EndRaid use case implementation.
    :type create_raid: CreateRaid
    :type rate_raid: RateRaid
    :type grade_raid: GradeRaid
    :type end_raid: EndRaid
    :return: Flask Blueprint.
    :rtype: Blueprint

    Implements the following routes:

    * */<prefix>/raid* (POST)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/raid \\
            -X POST --data @examples/json/create_raid.json \\
            -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "Raid created successfully",
             "raid": {}
         }

    * */<prefix>/raid/<int:raid_id>/rate* (PUT)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/raid/1/rate \\
             -X PUT --data @examples/json/rate_raid.json \\
             -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "Raid rated successfully"
         }

    * */<prefix>/raid/<int:raid_id>/end/* (PUT)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/raid/1/end \\
             -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "raid finished successfully",
             "score": "Gang's score: 10. Sheriff's score on raid 'raid': 10"
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
        """rate_raid_endpoint receives rates for a Raid and executes
           the Rate Raid use case.

        :param raid_id: Id of the Raid to be rated
        :type raid_id: Integer
        :return: Flask Response.
        :rtype: Response
        """
        data = request.get_json()
        outlaw_id = data.get('outlaw_id')
        rate = data.get('rate')
        score = Score(**rate)
        rate_raid.execute(RateRaidRequest(raid_id, outlaw_id, score))

        message = {'message': 'Raid rated successfully'}

        return jsonify(message)

    @blueprint_raid.route("/raid/<int:raid_id>/end",
                          methods=['PUT'])
    def end_raid_endpoint(raid_id: int) -> Response:
        """end_raid_endpoint receives id for a Raid and executes
           the Grade Raid and End Raid use cases.

        :param raid_id: Id of the Raid to be finished
        :type raid_id: Integer
        :return: Flask Response.
        :rtype: Response
        """

        grade = grade_raid.execute(GradeRaidRequest(raid_id))
        score_result = end_raid.execute(EndRaidRequest(raid_id, grade))

        message = {'message': 'raid finished successfully',
                   'score': score_result}

        return jsonify(message)

    return blueprint_raid
