import inject
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from typing import List


class ListGangs:
    """Class ListGangs implements the list gangs use case.
    :param gang_repository: Repository managing the Gang domain entities.
    :type gang_repository: GangRepository.
    """

    @inject.autoparams()
    def __init__(self, gang_repository: GangRepository):
        self.__gang_repository = gang_repository

    def execute(self, outlaw_id: int) -> List[Gang]:
        """execute is the actual action of the List Gangs use case.
        :param outlaw_id: ID of the Outlaw performing the action.
        :type outlaw_id: int.
        :returns: List[Gang] -- the list of gangs.
        """

        gangs = list()
        all_gangs = self.__gang_repository.all()

        for gang in all_gangs:
            for outlaw in gang.members:
                if outlaw_id == outlaw.id:
                    gangs.append(gang)

        return gangs
