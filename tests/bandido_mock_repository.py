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

