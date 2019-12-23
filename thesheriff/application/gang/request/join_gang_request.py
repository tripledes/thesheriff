class JoinGangRequest:
    """Class JoinGangRequest holds data required to join a Gang.

    :param gang_id: Id of the Gang.
    :type gang_id: Integer
    :param outlaw_id: Id of the Outlaw generating the request.
    :type outlaw_id: Integer
    """

    def __init__(self, gang_id: int, outlaw_id: int):
        self.gang_id = gang_id
        self.outlaw_id = outlaw_id
