import inject
from typing import NoReturn

from thesheriff.application.raid.request.rate_raid_request import \
    RateRaidRequest
from thesheriff.domain.raid.repository.raid_repository import RaidRepository
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.domain.outlaw.score import Score


class RateRaid:
    """Class RateRaid implements the Raid rating use case.

    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository
    :param raid_repository: Repository managing Raid domain entities.
    :type raid_repository: RaidRepository
    """

    @inject.autoparams()
    def __init__(
        self, outlaw_repository: OutlawRepository,
        raid_repository: RaidRepository
    ):
        self.__raid_repository = raid_repository
        self.__outlaw_repository = outlaw_repository

    def execute(
            self, request: RateRaidRequest
    ) -> NoReturn:
        """execute is the actual action of the Raid rating use case.

        :param request: the RateRaidRequest holding all the data
        :type request: RateRaidRequest
        :return: No value returned.
        :rtype: NoReturn
        """
        outlaw = self.__outlaw_repository.of_id(request.outlaw_id)
        raid = self.__raid_repository.of_id(request.raid_id)

        if outlaw:
            raid.add_rate(request.score.value())
            self.__raid_repository.update_rates(raid)
            return

        raise Exception("No outlaw found with Id", request.outlaw_id)
