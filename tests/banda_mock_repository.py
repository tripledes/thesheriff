from typing import NoReturn

from thesheriff.domain.banda.banda import Banda
from thesheriff.domain.banda.repository.banda_repository import BandaRepository
from thesheriff.domain.bandido import Bandido


class BandaMockRepository(BandaRepository):

    def of_id(self, banda_id: int) -> Banda:
        pass

    def add(self, nueva_banda: Banda) -> NoReturn:
        pass

    def update(self, mod_banda: Banda) -> NoReturn:
        pass

    def remove(self, banda_id: int) -> NoReturn:
        pass

    def all(self) -> [Banda]:
        banda1 = Banda(1, "Banda1")
        banda2 = Banda(2, "Banda2")
        banda3 = Banda(3, "Banda3")

        bandido1 = Bandido(1, "B1", "b1@yopmail.com")
        bandido2 = Bandido(2, "B2", "b2@yopmail.com")
        bandido3 = Bandido(3, "B3", "b3@yopmail.com")

        miembros_banda1 = [bandido1, bandido2]
        miembros_banda2 = [bandido2, bandido3]
        miembros_banda3 = [bandido1, bandido3]

        banda1.add_miembros(miembros_banda1)
        banda2.add_miembros(miembros_banda2)
        banda3.add_miembros(miembros_banda3)

        return [banda1, banda2, banda3]