import inject
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from typing import List


class ListGangs:
    """Class ListGangs implements the list all gangs use case.

    :param gang_repository: Repository managing Gang domain entities.
    :type gang_repository: GangRepository
    """

    @inject.autoparams()
    def __init__(self, gang_repository: GangRepository):
        self.__gang_repository = gang_repository

    def execute(self) -> List[Gang]:
        """execute is the actual action of listing all gangs use case.

        :return: All the stored gangs.
        :rtype: List[Gang]
        """
        return self.__gang_repository.all()
