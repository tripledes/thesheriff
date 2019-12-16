import abc
from ...raid.raid import Raid
from typing import NoReturn


class RaidRepository(abc.ABC):
    """Interface RaidRepository, defines how all raid repository
    implementations will behave.
    """

    @abc.abstractmethod
    def of_id(self, raid_id: int) -> Raid:
        pass

    @abc.abstractmethod
    def add(self, new_raid: Raid) -> NoReturn:
        pass
