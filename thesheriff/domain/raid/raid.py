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
    :param outlaws: List of Outlaws invited to the Raid.
    :type outlaws: List[Outlaw]
    :param location: Restaurant location.
    :type location: String
    :param sheriff: The Raid organizer.
    :type sheriff: Sheriff
    :param gang: Gang where the raid is organized.
    :type gang: Gang
    :param date: Date and time when the raid happens.
    :type date: datetime.datetime
    :param raid_id: Optional, Raid Id.
    :type raid_id: Integer
    """

    def __init__(
            self,
            name: str,
            location: str,
            sheriff: Sheriff,
            gang: Gang,
            date: datetime,
            raid_id: Optional[int] = None,
            outlaws: Optional[Outlaw] = []
    ):
        self.name = name
        self.location = location
        self.sheriff = sheriff
        self.gang = gang
        self.date = date
        self.rates = []
        self.id = raid_id
        self.outlaws = outlaws

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

        :return: If each member has rated the Raid.
        :rtype: Bool
        """
        return len(self.rates) == len(self.outlaws)

    def join(self, outlaw: Outlaw) -> NoReturn:
        """Method join, joins an Outlaw into a Gang.

        :param outlaw: The Outlaw joining this Gang.
        :type outlaw: Outlaw
        :return: No value returned.
        :rtype: NoReturn
        """
        self.outlaws.append(outlaw)
