import inject
from datetime import datetime
from thesheriff.application.raid.request.create_raid_request import \
    CreateRaidRequest
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.repository.outlaw_repository \
    import OutlawRepository
from thesheriff.domain.outlaw.sheriff import Sheriff
from thesheriff.domain.raid.raid import Raid, DEFAULT_DATETIME_FORMAT
from thesheriff.domain.raid.repository.raid_repository import RaidRepository


class CreateRaid:
    """Class CreateRaid implements the Create Raid use case.

    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository
    :param gang_repository: Repository managing Gang domain entities.
    :type gang_repository: GangRepository
    :param raid_repository: Repository managing Raid domain entities.
    :type raid_repository: RaidRepository
    """

    @inject.autoparams()
    def __init__(
            self,
            outlaw_repository: OutlawRepository,
            gang_repository: GangRepository,
            raid_repository: RaidRepository
    ):
        self.__outlaw_repository = outlaw_repository
        self.__gang_repository = gang_repository
        self.__raid_repository = raid_repository

    def execute(self, request: CreateRaidRequest) -> Raid:
        """execute is the actual action of listing all gangs use case.

        :param request: Request object with details for creating a Raid.
        :type request: CreateRaidRequest
        :return: The created Raid.
        :rtype: Raid
        """
        sheriff = self.__get_sheriff_or_fail(request)
        gang = self.__get_gang_or_fail(request)
        outlaws = self.__get_outlaws_or_fail(request)

        date = datetime.strptime(request.date, DEFAULT_DATETIME_FORMAT)
        raid_id = 0

        raid = Raid(
            request.name,
            request.location,
            sheriff,
            gang,
            date,
            raid_id,
            outlaws
        )

        self.__raid_repository.add(raid)

        return raid

    def __get_sheriff_or_fail(self, request: CreateRaidRequest) -> Sheriff:
        sheriff = self.__outlaw_repository.of_id(request.sheriff_id)
        if sheriff is None:
            raise Exception('Sheriff with id: {0} does not exist.'
                            .format(request.sheriff_id))
        sheriff = Sheriff(sheriff)
        return sheriff

    def __get_gang_or_fail(self, request: CreateRaidRequest) -> Gang:
        gang = self.__gang_repository.of_id(request.gang_id)
        if gang is None:
            raise Exception('Gang with id: {0} does not exist.'
                            .format(request.gang_id))
        return gang

    def __get_outlaws_or_fail(self, request: CreateRaidRequest) -> [Outlaw]:
        outlaws = []
        all_outlaws = self.__outlaw_repository.all()
        if outlaws is None or len(all_outlaws) < 1:
            raise Exception('Outlaws does not exist')

        for outlaw in all_outlaws:
            if outlaw.id in request.outlaw_ids:
                outlaws.append(outlaw)

        return outlaws
