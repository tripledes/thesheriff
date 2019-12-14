from typing import NoReturn

from thesheriff.domain.bandido import BandidoRepository, Bandido


class BandidoMockRepository(BandidoRepository):

    def __init__(self):
        self.bandido = None

    def of_id(self, bandido_id) -> Bandido:
        return self.bandido

    def add(self, new_bandido: Bandido) -> NoReturn:
        self.bandido = new_bandido

    def update(self, mod_bandido: Bandido) -> NoReturn:
        self.bandido = mod_bandido

    def remove(self, bandido_id: int) -> NoReturn:
        self.bandido = None

    def get_amigos(self, bandido_id: int) -> [Bandido]:
        bandido_1 = Bandido(1, "Bandido1", "b1@yopmail.com")
        bandido_2 = Bandido(2, "Bandido2", "b2@yopmail.com")
        bandido_3 = Bandido(3, "Bandido3", "b3@yopmail.com")

        return [bandido_1, bandido_2, bandido_3]

