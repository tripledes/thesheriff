import inject

from thesheriff.application.gang.request.create_gang_request import \
    CreateGangRequest
from thesheriff.domain.gang.gang_factory import GangFactory
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from thesheriff.domain.gang.gang import Gang


class CreateGang:
    """Class CreateGang implements the gang creation use case.

    :param gang_repository: Repository managing Gang domain entities.
    :type gang_repository: GangRepository
    """

    @inject.autoparams()
    def __init__(self, gang_repository: GangRepository):
        self.__gang_repository = gang_repository

    def execute(self, request: CreateGangRequest) -> Gang:
        """execute is the actual action of the Create Gang use case.

        :param request: Request object holding the Gang details.
        :type request: CreateGangRequest
        :return: The created Gang.
        :rtype: Gang
        """
        gang = GangFactory.create(request.owner_id, request.name)
        self.__gang_repository.add(gang)
        return gang
