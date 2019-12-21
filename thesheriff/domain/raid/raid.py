from datetime import datetime
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from typing import NoReturn, Optional, List


class Raid:
    """Class Raid represents the Asalto entity.
    :param name: The Raid given name.
    :type name: String.
    :param outlaws: List of Outlaws invited to the Raid.
    :type outlaws: List[Outlaw].
    :param location: Restaurant location.
    :type location: String.
    :param sheriff: The Raid organizer.
    :type sheriff: Sheriff.
    :param gang: Gang where the raid is organized.
    :type gang: Gang.
    :param date: Date and time when the raid happens.
    :type date: datetime.datetime.
    :param id: Optional, Raid Id.
    :type id: Integer.
    """

    def __init__(
        self, name: str, location: str,
        sheriff: Sheriff, gang: Gang, date: datetime
    ):
        self.name = name
        self.outlaws = list()
        self.location = location
        self.sheriff = sheriff
        self.gang = gang
        self.rates = []
        self.__id = None

    def add_rate(self, rate: float) -> NoReturn:
        """Method add_rate, adds a new rate for the Raid.
        :param rate: The rate to be added.
        :type rate: Float.
        :returns: NoReturn -- no value returned.
        """
        self.rates.append(rate)

    def could_finish(self) -> bool:
        """Method could_finish.
        :returns: Bool -- If each member has rated the Raid.
        """
        return len(self.rates) == len(self.outlaws)

    def join(self, outlaw: Outlaw):
        self.outlaws.append(outlaw)
