from thesheriff.domain.asalto import Asalto
from thesheriff.domain.asalto.asalto_repository import AsaltoRepository
from thesheriff.domain.bandido.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.puntuacion import Puntuacion

class PuntuarAsalto:
    def __init__(self, asalto: Asalto, bandidoRepository : BandidoRepository, asaltoRepository: AsaltoRepository):
        self.asalto = asalto
        self.asaltoRepository = asaltoRepository
        self.bandidoRepository = bandidoRepository

    def execute(self, bandido_id, puntuacion : Puntuacion):
        bandido = self.bandidoRepository.of_id(bandido_id)

        if(bandido):
            self.asalto.nuevaPuntuacion(puntuacion.value())
            self.asaltoRepository.update(self.asalto)

