from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido_repository import BandidoRepository


class CalificarAsalto:

    def __init__(self, asalto: Asalto, bandidoRepository : BandidoRepository):
        self.asalto = asalto
        self.bandidoRepository = bandidoRepository

    def execute(self):
        notaFinal = 0
        puntosCantidad = self.asalto.notas.__len__()
        if(puntosCantidad > 0):
            for nota in self.asalto.notas:
                notaFinal += nota

            notaFinal = notaFinal / puntosCantidad
            self.asalto.sheriff.actualizarPuntos(notaFinal)
            self.bandidoRepository.update(self.asalto.sheriff)

        return notaFinal
