from thesheriff.domain.raid.repository.raid_repository import RaidRepository


class EndRaid:

    def __init__(self, raid_repository: RaidRepository):
        self.raid_repository = raid_repository

    def execute(self, raid_id: int, raid_score: int):
        raid = self.raid_repository.of_id(raid_id=raid_id)

        if(not raid.could_finish()):
            raise Exception('Raid can not be finished until all outlaws have ranked it.')

        score_gang = 0
        for outlaw in raid.outlaws:
            score_gang += outlaw.score

        #FIXME: send email with gang updated score and sherrif's score in this raid

        return "Gang's score: {}. Sheriff's score on raid '{}': {}".format(score_gang, raid.name, raid_score)
