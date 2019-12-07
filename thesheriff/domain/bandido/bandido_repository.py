import abc

from thesheriff.domain.bandido import Bandido
from typing import NoReturn


class BandidoRepository(abc.ABC):
    @abc.abstractmethod
    def of_id(self, bandido_id: int) -> Bandido:
        pass

    @abc.abstractmethod
    def add(self, new_bandido: Bandido) -> NoReturn:
        pass

    @abc.abstractmethod
    def update(self, mod_bandido: Bandido) -> NoReturn:
        pass

    @abc.abstractmethod
    def remove(self, bandido_id: int) -> NoReturn:
        pass
