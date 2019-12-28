from datetime import datetime
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from typing import NoReturn, Optional, List


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
    :type date: String
    :param raid_id: Optional, Raid Id.
    :type raid_id: Integer
    :param rates: Optional, list with assigned rates.
    :type: rates: List[float]
    """

    DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(
            self,
            name: str,
            members: List[Outlaw],
            sheriff: Sheriff,
            gang: Gang,
            location: str,
            date: str,
            raid_id: Optional[int] = None,
            rates: Optional[List[float]] = list()
    ):
        self.name = name
        self.location = location
        self.sheriff = sheriff
        self.gang = gang
        self.date = datetime.strptime(date, self.DEFAULT_DATETIME_FORMAT)
        self.rates = rates
        self.id = raid_id
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
        self.members.append(outlaw)
