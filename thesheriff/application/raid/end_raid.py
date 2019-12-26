from thesheriff.domain.raid.repository.raid_repository import RaidRepository


class EndRaid:
    """Class EndRaid implements the End a Raid use case.

    :param raid_repository: Repository managing Raid domain entities.
    :type raid_repository: RaidRepository
    """

    def __init__(self, raid_repository: RaidRepository):
        self.raid_repository = raid_repository

    def execute(self, raid_id: int, raid_score: int):
        """execute is the actual action of the Raid rating use case.

        :param raid_id: ID of the Raid to be end.
        :type raid_id: Integer
        :param raid_score: Score assign to the Raid.
        :type raid_score: Integer
        :return: Message with scores.
        :rtype: String
        """
        raid = self.raid_repository.of_id(raid_id=raid_id)

        if(not raid.could_finish()):
            raise Exception(
                'Raid can not be finished until all outlaws have ranked it.')

        score_gang = 0
        for outlaw in raid.members:
            score_gang += outlaw.score

        # FIXME: send email with gang updated score
        # and sherrif's score in this raid

        return "Gang's score: {}. Sheriff's score on raid '{}': {}".format(
            score_gang, raid.name, raid_score)
