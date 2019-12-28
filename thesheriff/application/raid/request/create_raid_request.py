from datetime import datetime
from typing import List


class CreateRaidRequest:
    """Class CreateRaidRequest holds data required to create a Raid.

    :param name: Raid's given name.
    :type name: String
    :param date: Date and time for the Raid.
    :type date: String
    :param location: Location of the Raid.
    :type location: String
    :param gang_id: Id of the Gang where the Raid is being organized.
    :type gang_id: Integer
    :param sheriff_id: Id of the Sheriff organizing the Raid.
    :type sheriff_id: Integer
    :param outlaw_ids: List of Outlaw Ids invited to the Raid.
    :type outlaw_ids: List[Integer]
    """

    def __init__(
        self,
        name: str,
        date: str,
        location: str,
        gang_id: int,
        sheriff_id: int,
        outlaw_ids: List[int]
    ):
        self.name = name
        self.date = date
        self.location = location
        self.gang_id = gang_id
        self.sheriff_id = sheriff_id
        self.outlaw_ids = outlaw_ids
