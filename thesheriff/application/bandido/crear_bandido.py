import inject

from thesheriff.application.bandido.request.crear_bandido_request import CrearBandidoRequest
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.bandido_factory import BandidoFactory
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository


class CrearBandido:

    @inject.autoparams()
    def __init__(self, bandido_repository: BandidoRepository):
        self.bandido_repository = bandido_repository

    def execute(self, request: CrearBandidoRequest) -> Bandido:
        new_bandido = BandidoFactory.crear(request.nombre, request.correo)
        self.bandido_repository.add(new_bandido)
        return new_bandido
