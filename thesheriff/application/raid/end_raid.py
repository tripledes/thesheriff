from thesheriff.domain.raid.repository.raid_repository import RaidRepository
from thesheriff.application.raid.request.end_raid_request import EndRaidRequest


class EndRaid:
    """Class EndRaid implements the End a Raid use case.

    :param raid_repository: Repository managing Raid domain entities.
    :type raid_repository: RaidRepository
    """

    def __init__(self, raid_repository: RaidRepository):
        self.raid_repository = raid_repository

    def execute(self, request: EndRaidRequest):
        """execute is the actual action of the End a Raid use case.

        :param request: Request holding the Raid details to be ended.
        :type request: EndRaidRequest
        :return: Message with scores.
        :rtype: String
        """
        raid = self.raid_repository.of_id(raid_id=request.raid_id)

        if(not raid.could_finish()):
            raise Exception(
                'Raid can not be finished until all outlaws have ranked it.')

        score_gang = 0.0
        for outlaw in raid.members:
            score_gang += outlaw.score

        # FIXME: send email with gang updated score
        # and sherrif's score in this raid

        return "Gang's score: {}. Sheriff's score on raid '{}': {}".format(
            score_gang, raid.name, request.raid_score)
