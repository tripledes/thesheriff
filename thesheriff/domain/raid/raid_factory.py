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
        id: Optional[int], name: str, outlaws: List[Outlaw],
        sheriff: Sheriff, gang: Gang, location: str, date: datetime
    ) -> Raid:
        """Method create, produces a Raid instance.

        :param id: Optional, Raid's Id.
        :type id: Integer
        :param name: Outlaw's given name.
        :type name: String
        :param outlaws: Outlaws invited to raid.
        :type outlaws: List[Outlaw]
        :param location: Location of the raid.
        :type location: String
        :param sheriff: The Outlaw organizing the Raid.
        :type sheriff: Sheriff
        :param gang: Gang this Raid is organized for.
        :type gang: Gang
        :param date: Raid's date and time.
        :type date: datetime.datetime
        :return: The produced Raid.
        :rtype: Raid
        """
        return Raid(
            name, outlaws, location, sheriff, gang, date, id)
