from thesheriff.domain.bandido import BandidoRepository, Bandido
from thesheriff.domain.bandido.bandido_factory import BandidoFactory


class CrearBandido:

    def __init__(self, bandido_repository: BandidoRepository):
        self.bandido_repository = bandido_repository

    def execute(self, name, correo) -> Bandido:
        new_bandido = BandidoFactory.crear(name, correo)
        self.bandido_repository.add(new_bandido)
        return new_bandido
