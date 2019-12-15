import inject
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.bandido import Bandido

class ListarAmigos:

    @inject.autoparams()
    def __init__(self, bandido_repository: BandidoRepository):
        self.bandidoRepository = bandido_repository

    def execute(self, bandido_id) -> [Bandido]:
        lista_amigos = self.bandidoRepository.get_amigos(bandido_id)
        return lista_amigos
