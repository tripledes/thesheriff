from typing import List, NoReturn


class Gang:
    """Class Gang, the Gang domain entity class.
    :param owner_id: Outlaw's Id, owner of the new Gang.
    :type owner_id: Integer.
    :param name: Given name of the Gang.
    :type name: String.
    """

    def __init__(self, owner_id: int, name: str):
        # TODO(all)
        # It would seem only logical that the owner is also a member.
        # Should owner_id be an actual Outlaw instance?
        self.name = name
        self.members = list()
        self.created_raids = 0
        self.owner_id = owner_id
        self.id = None

        if self.name is None:
            raise Exception('Gang name required')

    def members(self) -> list:
        """Method members.
        :returns: List[Outlaw] -- the list of Outlaws, members of the Gang.
        """
        return self.members

    def add_members(self, members: list) -> NoReturn:
        """Method add_members.
        :param members: List of Outlaws on the Gang.
        :type members: list
        :returns: NoReturn -- no value returned.
        """
        # TODO(all)
        # Should this be singular? add_member.
        self.members = members
