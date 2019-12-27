import inject
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.domain.outlaw.outlaw import Outlaw
from typing import List


class ListFriends:
    """Class ListFriends implements the List Outlaw's Friends use case.

    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository
    """

    @inject.autoparams()
    def __init__(self, outlaw_repository: OutlawRepository):
        self.__outlaw_repository = outlaw_repository

    def execute(self, outlaw_id) -> List[Outlaw]:
        """execute is the actual action of the List Outlaw's Friends use case.

        :param outlaw_id: ID of the Outlaw for which to list friends.
        :type outlaw_id: Integer
        :return: The list of friends.
        :rtype: List[Outlaw]
        """

        friends = self.__outlaw_repository.get_friends(outlaw_id)
        return friends
