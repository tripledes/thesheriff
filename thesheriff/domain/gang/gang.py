from typing import NoReturn, Optional


class Gang:
    """Class Gang, the Gang domain entity class.

    :param owner_id: Outlaw's Id, owner of the new Gang.
    :type owner_id: Integer
    :param name: Given name of the Gang.
    :type name: String
    :param gang_id: Optional, Gang Id.
    :type gang_id: Integer
    """

    def __init__(
        self, owner_id: int, name: str, gang_id: Optional[int] = None
    ):
        # TODO(all)
        # Verify owner_id is of an existing outlaw
        self.name = name
        self.members = list()
        self.created_raids = 0
        self.owner_id = owner_id
        self.id = gang_id

        if self.name is None:
            raise Exception('Gang name required')

    def members(self) -> list:
        """Method members.

        :return: The list of Outlaws, members of the Gang.
        :rtype: list
        """
        return self.members

    def add_members(self, members: list) -> NoReturn:
        """Method add_members.

        :param members: List of Outlaws on the Gang.
        :type members: List
        :return: No value returned.
        :rtype: NoReturn
        """
        # TODO(all)
        # Should this be singular? add_member.
        # It depends, if its a list, add_members is correct
        self.members = members
