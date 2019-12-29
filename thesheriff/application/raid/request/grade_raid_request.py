class GradeRaidRequest:
    """Class GradeRaidRequest holds data required to grade a Raid.

       :param raid_id: Id of the Raid to be ended.
       :type raid_id: Integer
       """

    def __init__(self, raid_id: int):
        self.raid_id = raid_id
