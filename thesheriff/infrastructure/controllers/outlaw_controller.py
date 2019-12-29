"""
thesheriff.infrastructure.controllers.outlaw_controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the RESTful part of the Outlaw use cases.

"""
import inject
from flask import Blueprint, jsonify, Response, request
from thesheriff.application.outlaw.create_outlaw import CreateOutlaw
from thesheriff.application.outlaw.invite_friend import InviteFriend
from thesheriff.application.outlaw.list_friends import ListFriends
from thesheriff.application.outlaw.list_gangs import ListGangs
from thesheriff.application.outlaw.request.create_outlaw_request import \
    CreateOutlawRequest
from thesheriff.application.outlaw.request.invite_friend_request import \
    InviteFriendRequest
from thesheriff.application.outlaw.request.list_friends_request import \
    ListFriendsRequest
from thesheriff.application.outlaw.request.list_gangs_request import \
    ListGangsRequest


@inject.autoparams()
def outlaw_controller(
        create_outlaw: CreateOutlaw, list_friends: ListFriends,
        list_gangs: ListGangs, invite_friend: InviteFriend
) -> Blueprint:
    """outlaw_controller holds the blueprint for all outlaw routes.

    :param create_outlaw: Create Outlaw use case implementation.
    :type create_outlaw: CreateOutlaw
    :param list_friends: List Friends use case implementation.
    :type list_friends: ListFriends
    :param list_gangs: List Gangs use case implementation.
    :type list_gangs: ListGangs
    :param invite_friend: InviteFiend use case implementation.
    :type invite_friend: InviteFriend
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
             "message": "Outlaw created successfully",
             "outlaw": {
                 "id": 1,
                 "name": "outlaw 1",
                 "email": "outlaw1@domain.net"
             }
         }

    * */<prefix>/outlaw/<int:outlaw_id>/friends* (GET)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/friends

      **Response Example:**

      .. code-block:: json

         {
             "message": "Success",
             "friends": [
                 {
                     "id": 1,
                     "name": "Outlaw1",
                     "email": "outlaw1@domain.net"
                 },
                 {
                     "id": 2,
                     "name": "Outlaw2",
                     "email": "outlaw2@domain.net"
                }
             ]
         }
    * */<prefix>/outlaw/<int:outlaw_id>/gangs* (GET)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/gangs

      **Response Example:**

      .. code-block:: json

         {
             "message": "Success",
             "gangs": [
                 {"id": 1, "name": "The Band 1"},
                 {"id": 2, "name": "The Band 2"}
             ]
         }

    * */<prefix>/outlaw/invite_friend/* (POST)

      **Request Example:**

      .. code-block:: console

         $ curl localhost:5000/api/<version>/outlaw/1/invite_friend/ \\
            -X POST --data @examples/json/invite_friend.json \\
            -H 'Content-Type: application/json'

      **Response Example:**

      .. code-block:: json

         {
             "message": "Invitation sent successfully"
         }
    """
    blueprint_outlaw = Blueprint('outlaw', __name__)

    @blueprint_outlaw.route('/outlaw', methods=['POST'])
    def create_outlaw_endpoint() -> Response:
        data = request.get_json()
        # TODO(all): if outlaw is None we should return an HTTP error
        new_outlaw = data.get('outlaw')

        outlaw = create_outlaw.execute(CreateOutlawRequest(
            new_outlaw.get('name'), new_outlaw.get('email')))

        result = dict({'id': outlaw.id, 'name': outlaw.name,
                       'email': outlaw.email})

        message = {'message': 'Outlaw created successfully', 'outlaw': result}

        return jsonify(message)

    @blueprint_outlaw.route('/outlaw/<int:outlaw_id>/friends', methods=['GET'])
    def get_friends_endpoint(outlaw_id: int) -> Response:
        friends = list_friends.execute(ListFriendsRequest(outlaw_id))
        result = list()
        for friend in friends:
            result.append(
                {'id': friend.id, 'name': friend.name}
            )

        message = {'message': "Success", 'friends': result}

        return jsonify(message)

    @blueprint_outlaw.route('/outlaw/<int:outlaw_id>/gangs', methods=['GET'])
    def get_gangs_endpoint(outlaw_id: int) -> Response:
        outlaw_gangs = list_gangs.execute(ListGangsRequest(outlaw_id))
        result = list()
        for gang in outlaw_gangs:
            result.append(
                {'id': gang.id, 'name': gang.name}
            )

        message = {'message': 'Success', 'gangs': result}

        return jsonify(message)

    @blueprint_outlaw.route("/outlaw/<int:outlaw_id>/invite_friend/",
                            methods=['POST'])
    def invite_friend_endpoint(outlaw_id: int) -> Response:
        data = request.get_json()
        mail_address = data.get('receiver_mail_address')
        invite_friend.execute(InviteFriendRequest(outlaw_id, mail_address))
        message = {'message': 'Invitation sent successfully'}
        return jsonify(message)

    return blueprint_outlaw
