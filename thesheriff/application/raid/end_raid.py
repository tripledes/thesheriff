import inject

from thesheriff.domain.mail.mail_factory \
    import MailFactory
from thesheriff.domain.mail.notifier.mail_notifier \
    import MailNotifier
from thesheriff.domain.outlaw.repository.outlaw_repository \
    import OutlawRepository
from thesheriff.domain.outlaw.sheriff_factory \
    import SheriffFactory
from thesheriff.domain.raid.repository.raid_repository \
    import RaidRepository
from thesheriff.application.raid.request.end_raid_request \
    import EndRaidRequest


class EndRaid:
    """Class EndRaid implements the End a Raid use case.

    :param raid_repository: Repository managing Raid domain entities.
    :type raid_repository: RaidRepository
    """
    @inject.autoparams()
    def __init__(self, mail_notifier: MailNotifier,
                 raid_repository: RaidRepository,
                 outlaw_repository: OutlawRepository):
        self.__mail_notifier = mail_notifier
        self.__raid_repository = raid_repository
        self.__outlaw_repository = outlaw_repository

    def execute(self, request: EndRaidRequest):
        """execute is the actual action of the End a Raid use case.

        :param request: Request holding the Raid details to be ended.
        :type request: EndRaidRequest
        :return: Message with scores.
        :rtype: String
        """
        raid = self.__raid_repository.of_id(raid_id=request.raid_id)
        owner = self.__outlaw_repository.of_id(raid.sheriff.id)
        raid.sheriff = SheriffFactory.create(owner)

        if not raid.could_finish():
            raise Exception(
                'Raid can not be finished until all outlaws have ranked it.')

        gang_score = raid.gang.score()

        mail = MailFactory.mail_raid_finished(raid, request.raid_score)
        self.__mail_notifier.send(mail=mail)

        return "Gang's score: {}. Sheriff's score on raid '{}': {}".format(
            gang_score, raid.name, request.raid_score)
