import inject
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.application.gang.request.join_gang_request import \
    JoinGangRequest
from typing import NoReturn


class JoinGang:
    """JoinGang class implements the Join Gang use case.

    :param outlaw_repository: Repository for managing Outlaw entities.
    :type outlaw_repository: OutlawRepository
    :param gang_repository: Repository for managing Gang entities.
    :type gang_repository: GangRepository
    """

    @inject.autoparams()
    def __init__(
        self, outlaw_repository: OutlawRepository,
        gang_repository: GangRepository
    ):
        self.__outlaw_repository = outlaw_repository
        self.__gang_repository = gang_repository

    def execute(self, request: JoinGangRequest) -> NoReturn:
        """execute is the actual action of the Join Gang use case.

        :param request: Request holding details for joining a Gang.
        :type request: JoinGangRequest
        :return: No value returned.
        :rtype: NoReturn
        """
        gang = self.__gang_repository.of_id(request.gang_id)
        outlaw = self.__outlaw_repository.of_id(request.outlaw_id)
        outlaw.join_gang(gang)
        self.__outlaw_repository.update(outlaw)
