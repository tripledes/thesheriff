from datetime import datetime
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from typing import NoReturn, Optional, List

DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class Raid:
    """Class Raid represents the Raid entity.

    :param name: The Raid given name.
    :type name: String
    :param members: List of Outlaws invited to the Raid.
    :type members: List[Outlaw]
    :param sheriff: The Raid organizer.
    :type sheriff: Sheriff
    :param gang: Gang where the raid is organized.
    :type gang: Gang
    :param location: Restaurant location.
    :type location: String
    :param date: Date and time when the raid happens.
    :type date: datetime.datetime
    :param id: Optional, Raid Id.
    :type id: Integer
    """

    def __init__(
            self,
            name: str,
            members: List[Outlaw],
            sheriff: Sheriff,
            gang: Gang,
            location: str,
            date: datetime,
            id: Optional[int] = None
    ):
        self.name = name
        self.location = location
        self.sheriff = sheriff
        self.gang = gang
        self.date = date
        self.rates = []
        self.id = id
        self.members = members

    def add_rate(self, rate: float) -> NoReturn:
        """Method add_rate, adds a new rate for the Raid.

        :param rate: The rate to be added.
        :type rate: Float
        :return: No value returned.
        :rtype: NoReturn
        """
        self.rates.append(rate)

    def could_finish(self) -> bool:
        """Method could_finish.

        :return: Whether each member has rated the Raid.
        :rtype: Bool
        """
        return len(self.rates) == len(self.members)

    def join(self, outlaw: Outlaw) -> NoReturn:
        """Method join, joins an Outlaw into a Raid.

        :param outlaw: The Outlaw joining this Raid.
        :type outlaw: Outlaw
        :return: No value returned.
        :rtype: NoReturn
        """
        # TODO(all): consider if this method is needed
        self.members.append(outlaw)
