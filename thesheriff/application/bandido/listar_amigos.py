from thesheriff.domain.bandido.bandido_repository import BandidoRepository


class ListarAmigos:
    def __init__(self, bandido_repository: BandidoRepository):
        self.bandidoRepository = bandido_repository

    def execute(self, bandido_id):
        lista_amigos = self.bandidoRepository.lista_amigos(bandido_id)
        return lista_amigos
