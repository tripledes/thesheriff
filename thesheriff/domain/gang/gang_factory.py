from thesheriff.domain.gang.gang import Gang


class GangFactory(Gang):
    """Class GangFactory produces Gangs.
    """

    @staticmethod
    def create(owner_id: int, name: str) -> Gang:
        """Method create, produces a Gang instance.

        :param owner_id: Outlaw's Id, who is creating the Gang.
        :type owner_id: Integer
        :return: The created Gang.
        :rtype: Gang
        """
        return Gang(owner_id, name)
