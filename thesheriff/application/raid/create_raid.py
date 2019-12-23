from datetime import datetime

from thesheriff.application.raid.create_raid_request import CreateRaidRequest
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.repository.outlaw_repository \
    import OutlawRepository
from thesheriff.domain.outlaw.sheriff import Sheriff
from thesheriff.domain.raid.raid import Raid, DEFAULT_DATETIME_FORMAT
from thesheriff.domain.raid.repository.raid_repository import RaidRepository


class CreateRaid:
    def __init__(
            self,
            outlaw_repository: OutlawRepository,
            gang_repository: GangRepository,
            raid_repository: RaidRepository
    ):
        self.__outlaw_repository = outlaw_repository
        self.__gang_repository = gang_repository
        self.__raid_repository = raid_repository

    def execute(self, request: CreateRaidRequest):
        sheriff = self.get_sheriff_or_fail(request)
        gang = self.get_gang_or_fail(request)
        outlaws = self.get_outlaws_or_fail(request)

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

    def get_sheriff_or_fail(self, request: CreateRaidRequest) -> Sheriff:
        sheriff = self.__outlaw_repository.of_id(request.sheriff_id)
        if sheriff is None:
            raise Exception('Sheriff with id: {0} does not exist.'
                            .format(request.sheriff_id))
        sheriff = Sheriff(sheriff)
        return sheriff

    def get_gang_or_fail(self, request: CreateRaidRequest) -> Gang:
        gang = self.__gang_repository.of_id(request.gang_id)
        if gang is None:
            raise Exception('Gang with id: {0} does not exist.'
                            .format(request.gang_id))
        return gang

    def get_outlaws_or_fail(self, request: CreateRaidRequest) -> [Outlaw]:
        outlaws = []
        all_outlaws = self.__outlaw_repository.all()
        if outlaws is None or len(all_outlaws) < 1:
            raise Exception('Outlaws does not exist')

        for outlaw in all_outlaws:
            if outlaw.id in request.outlaw_ids:
                outlaws.append(outlaw)

        return outlaws
