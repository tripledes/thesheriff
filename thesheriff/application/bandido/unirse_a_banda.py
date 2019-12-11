import inject

from thesheriff.domain.banda.banda_repository import BandaRepository
from thesheriff.domain.bandido.bandido_repository import BandidoRepository


class UnirseABanda:

    @inject.autoparams()
    def __init__(self, bandido_repository: BandidoRepository, banda_repository: BandaRepository):
        self.bandido_repository = bandido_repository
        self.banda_repository = banda_repository

    def execute(self, id_banda: int, id_bandido: int):
        banda = self.banda_repository.of_id(id_banda)
        bandido = self.bandido_repository.of_id(id_bandido)
        bandido.unirse_a_banda(banda)
        self.bandido_repository.update(bandido)
