from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido_repository import BandidoRepository


class CalificarAsalto:

    def __init__(self, asalto: Asalto, bandido_repository: BandidoRepository):
        self.asalto = asalto
        self.bandidoRepository = bandido_repository

    def execute(self):
        nota_final = 0
        puntos_cantidad = self.asalto.notas.__len__()
        if puntos_cantidad > 0:
            for nota in self.asalto.notas:
                nota_final += nota

            nota_final = nota_final / puntos_cantidad
            self.asalto.sheriff.actualizar_puntos(nota_final)
            self.bandidoRepository.update(self.asalto.sheriff)

        return nota_final
