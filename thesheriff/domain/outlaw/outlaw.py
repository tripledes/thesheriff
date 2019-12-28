from thesheriff.domain.gang.gang import Gang
from typing import NoReturn, Optional, List


class Outlaw:
    """Class Outlaw represents the Outlaw domain entity.

    :param name: Outlaw's given name.
    :type name: String
    :param email: Outlaw's email address.
    :type email: String
    :param outlaw_id: Optional, Outlaw Id.
    :type outlaw_id: Integer
    """

    def __init__(
        self, name: str, email: str, outlaw_id: Optional[int] = None
    ):
        self.id = outlaw_id
        self.name = name
        self.email = email
        self.raids = list()
        self.friends = list()
        self.score = 0.0
        self.gangs = list()

    def join_gang(self, gang: Gang) -> NoReturn:
        """Method join_banda

        :param gang: The Gang instance to which to join
        :type gang: Gang
        :return: No returned value.
        :rtype: NoReturn
        """
        self.gangs.append(gang)

    def get_email(self) -> str:
        """Method get_email, returns Outlaw's email address.

        :return: The email address.
        :rtype: String
        """
        return self.email
