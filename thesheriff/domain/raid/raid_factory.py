from datetime import datetime
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from typing import List, Optional


class RaidFactory(Raid):
    """Class RaidFactory produces Raids.
    """

    @staticmethod
    def create(
        name: str, members: List[Outlaw], sheriff: Sheriff,
        gang: Gang, location: str, date: datetime,
        raid_id: Optional[int] = None,
        rates: Optional[List[float]] = list()
    ) -> Raid:
        """Method create, produces a Raid instance.

        :param name: Outlaw's given name.
        :type name: String
        :param members: Outlaws invited to raid.
        :type members: List[Outlaw]
        :param sheriff: The Outlaw organizing the Raid.
        :type sheriff: Sheriff
        :param gang: Gang this Raid is organized for.
        :type gang: Gang
        :param location: Location of the raid.
        :type location: String
        :param date: Raid's date and time.
        :type date: datetime.datetime
        :param raid_id: Optional, Raid's Id.
        :type raid_id: Integer
        :param rates: Optional, list with assigned rates.
        :type: rates: List[float]
        :return: The produced Raid.
        :rtype: Raid
        """
        return Raid(
            name, members, sheriff, gang, location, date, raid_id)
