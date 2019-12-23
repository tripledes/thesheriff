class CreateGangRequest:
    """Class JoinGangRequest holds data required to join a Gang.

    :param name: Name of the Gang.
    :type name: String
    :param owner_id: Id of the Outlaw creating the gang.
    :type owner_id: Integer
    """

    def __init__(self, owner_id: int, name: str):
        self.owner_id = owner_id
        self.name = name
