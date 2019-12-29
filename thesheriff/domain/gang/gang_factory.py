from typing import Optional

from thesheriff.domain.gang.gang import Gang


class GangFactory(Gang):
    """Class GangFactory produces Gangs.
    """

    @staticmethod
    def create(
            owner_id: int, name: str, gang_id: Optional[int] = None
    ) -> Gang:
        """Method create, produces a Gang instance.

        :param owner_id: Outlaw's Id, who is creating the Gang.
        :type owner_id: Integer
        :param name: Given name of the Gang.
        :type name: String
        :param gang_id: Optional, Gang's Id.
        :type gang_id: Integer
        :return: The created Gang.
        :rtype: Gang
        """

        if name is None:
            raise Exception('Gang name required')

        return Gang(owner_id, name, gang_id)

    @staticmethod
    def create_with_id(gang_id: int) -> Gang:
        """Method create, produces a Gang instance with just its Id.

        :param gang_id: Gang's Id.
        :type gang_id: Integer
        :return: The created Gang.
        :rtype: Gang
        """
        return Gang(None, "", gang_id)
