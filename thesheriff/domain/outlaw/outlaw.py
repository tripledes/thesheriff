from ..gang.gang import Gang
from typing import NoReturn, Optional, List


class Outlaw:
    """Class Outlaw represents the Outlaw domain entity.
    :param id: Optional, Bandido Id.
    :type id: Integer.
    :param name: Bandido's given name.
    :type name: String.
    :param email: Bandido's email address.
    :type email: String.
    :param score: Optional, Outlaw's general score.
    :type score: Integer.
    """

    def __init__(self, _id: int, name: str, email: str):
        self.id = _id
        self.name = name
        self.email = email
        self.raids = list()
        self.friends = list()
        self.score = 0
        self.gangs = list()

    def join_band(self, gang: Gang) -> NoReturn:
        """Method join_banda
        :param gang: The Gang instance to which to join
        :type gang: Gang
        """
        self.gangs.append(gang)

    def list_friends(self) -> list:
        """Method list_friends
        :returns: list -- The actual list of friends instances.
        """
        # TODO(all):
        # using List[Outlaw] as a return type produces a circular dependency
        # are we sure this method belongs here?
        return self.friends
