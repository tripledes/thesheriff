import abc
from ...outlaw.outlaw import Outlaw
from typing import List, NoReturn


class OutlawRepository(abc.ABC):
    """Interface OutlawRepository, defines how all outlaw repository
    implementations will behave.
    """

    @abc.abstractmethod
    def of_id(self, outlaw_id: int) -> Outlaw:
        pass

    @abc.abstractmethod
    def add(self, new_outlaw: Outlaw) -> Outlaw:
        pass

    @abc.abstractmethod
    def update(self, mod_outlaw: Outlaw) -> NoReturn:
        pass

    @abc.abstractmethod
    def remove(self, outlaw_id: int) -> NoReturn:
        pass

    @abc.abstractmethod
    def get_friends(self, outlaw_id: int) -> List[Outlaw]:
        pass

    @abc.abstractmethod
    def all(self) -> List[Outlaw]:
        pass
