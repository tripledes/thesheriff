class ListGangsRequest:
    """Class ListGangsRequest holds data required to get Outlaw's gangs.

        :param outlaw_id: Outlaw's id.
        :type outlaw_id: int
        """
    def __init__(self, outlaw_id: int):
        self.outlaw_id = outlaw_id
