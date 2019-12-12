import inject

from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.bandido_factory import BandidoFactory


class CrearBandido:

    @inject.autoparams()
    def __init__(self, bandido_repository: BandidoRepository):
        self.bandido_repository = bandido_repository

    def execute(self, name, correo) -> Bandido:
        new_bandido = BandidoFactory.crear(name, correo)
        self.bandido_repository.add(new_bandido)
        return new_bandido
