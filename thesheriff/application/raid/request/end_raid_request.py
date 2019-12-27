from datetime import datetime
from typing import List


class EndRaidRequest:
    """Class EndRaidRequest holds data required to end a Raid.

    :param raid_id: Id of the Raid to be ended.
    :type raid_id: Integer
    :param raid_score: Score assigned to the Raid.
    :type raid_score: Float
    """

    def __init__(
        self,
        raid_id: str,
        raid_score: float
    ):
        self.raid_id = raid_id
        self.raid_score = raid_score
