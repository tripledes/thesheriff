import abc

from typing import NoReturn
from thesheriff.domain.asalto import Asalto


class AsaltoRepository(abc.ABC):
    @abc.abstractmethod
    def of_id(self, asalto_id: int) -> Asalto:
        pass

    @abc.abstractmethod
    def add(self, new_asalto: Asalto) -> NoReturn:
        pass

    @abc.abstractmethod
    def update(self, mod_asalto: Asalto) -> NoReturn:
        pass
