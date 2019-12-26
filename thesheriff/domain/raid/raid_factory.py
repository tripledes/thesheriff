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
        gang: Gang, location: str, date: datetime, id: Optional[int] = None
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
        :param id: Optional, Raid's Id.
        :type id: Integer
        :return: The produced Raid.
        :rtype: Raid
        """
        return Raid(
            name, location, sheriff, gang, date, id, outlaws)
