import inject

from thesheriff.application.outlaw.request.list_gangs_request import \
    ListGangsRequest
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from typing import List


class ListGangs:
    """Class ListGangs implements the List Outlaw's Gangs use case.

    :param gang_repository: Repository managing the Gang domain entities.
    :type gang_repository: GangRepository
    """

    @inject.autoparams()
    def __init__(self, gang_repository: GangRepository):
        self.__gang_repository = gang_repository

    def execute(self, request: ListGangsRequest) -> List[Gang]:
        """execute is the actual action of the List Gangs use case.

        :param request: request object holding data to perform the action.
        :type request: ListGangsRequest
        :return: The list of gangs.
        :rtype: List[Gang]
        """

        gangs = list()
        all_gangs = self.__gang_repository.all()

        for gang in all_gangs:
            for outlaw in gang.members:
                if request.outlaw_id == outlaw.id:
                    gangs.append(gang)

        return gangs
