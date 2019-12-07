import abc

from thesheriff.domain.banda.banda import Banda
from typing import NoReturn

class BandaRepository(abc.ABC):

    @abc.abstractmethod
    def of_id(self, banda_id: int) -> Banda:
        pass

    @abc.abstractmethod
    def add(self, nueva_banda: Banda) -> NoReturn:
        pass

    @abc.abstractmethod
    def update(self, mod_banda: Banda) -> NoReturn:
        pass

    @abc.abstractmethod
    def remove(self, banda_id: int) -> NoReturn:
        pass

    @abc.abstractmethod
    def all(self) -> [Banda]:
        pass