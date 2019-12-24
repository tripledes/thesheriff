from thesheriff.domain.gang.gang import Gang
from typing import Optional


class GangFactory(Gang):
    """Class GangFactory produces Gangs.
    """

    @staticmethod
    def create(owner_id: int, name: str, id: Optional[int] = None) -> Gang:
        """Method create, produces a Gang instance.

        :param owner_id: Outlaw's Id, who is creating the Gang.
        :type owner_id: Integer
        :param name: Given name of the Gang.
        :type name: String
        :param id: Optional, Gang's Id.
        :type id: Integer
        :return: The created Gang.
        :rtype: Gang
        """
        return Gang(owner_id, name)
