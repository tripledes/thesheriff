from thesheriff.domain.outlaw.score import Score


class RateRaidRequest:
    """Class RateRaidRequest holds data required to rate a Raid.

        :param raid_id: Id of the Raid to be ended.
        :type raid_id: Integer
        :param outlaw_id: Id of the Outlaw performing the rate.
        :type outlaw_id: Integer
        :param score: the Outlaw's score rating.
        :type score: Score
        """

    def __init__(
            self,
            raid_id: int,
            outlaw_id: int,
            score: Score
    ):
        self.raid_id = raid_id
        self.outlaw_id = outlaw_id
        self.score = score
