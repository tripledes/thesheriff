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
        """execute is the actual action of the Raid rating use case.

        :param owner_id: ID of the Outlaw creating the Gang.
        :type owner_id: Integer.
        :param name: Given name of the Gang.
        :type name: String.
        :return: The created Gang.
        :rtype: Gang
        """
        gang = GangFactory.create(request.owner_id, request.name)
        self.__gang_repository.add(gang)
        return gang
