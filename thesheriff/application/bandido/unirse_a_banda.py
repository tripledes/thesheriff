from typing import NoReturn

import inject

from thesheriff.domain.banda.repository.banda_repository import BandaRepository
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository
from thesheriff.application.banda.request.unirse_a_banda_request import UnirseABandaRequest


class UnirseABanda:

    @inject.autoparams()
    def __init__(self, bandido_repository: BandidoRepository, banda_repository: BandaRepository):
        self.bandido_repository = bandido_repository
        self.banda_repository = banda_repository

    def execute(self, request: UnirseABandaRequest) -> NoReturn:
        banda = self.banda_repository.of_id(request.banda_id)
        bandido = self.bandido_repository.of_id(request.badido_id)
        bandido.unirse_a_banda(banda)
        self.bandido_repository.update(bandido)
