import abc
from ...gang.gang import Gang
from typing import NoReturn, List


class GangRepository(abc.ABC):
    """Interface GangRepository, defines how all gang repository
    implementations will behave.
    """

    @abc.abstractmethod
    def of_id(self, gang_id: int) -> Gang:
        pass

    @abc.abstractmethod
    def all(self) -> List[Gang]:
        pass

    @abc.abstractmethod
    def add(self, new_gang: Gang) -> Gang:
        pass

    @abc.abstractmethod
    def update(self, mod_gang: Gang) -> NoReturn:
        pass

    @abc.abstractmethod
    def remove(self, gang_id: int) -> NoReturn:
        pass
