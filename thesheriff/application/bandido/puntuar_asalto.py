from thesheriff.domain.bandido.puntuacion import Puntuacion

class PuntuarAsalto:
    def __init__(self, asalto, bandidoRepository):
        self.asalto = asalto
        self.bandidoRepository = bandidoRepository

    def execute(self, bandido_id, puntuacion : Puntuacion):
        bandido = self.bandidoRepository.of_id(bandido_id)

        if(bandido):
            self.asalto.puntuar(puntuacion.value())

