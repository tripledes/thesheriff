from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository


class CalificarAsalto:

    def __init__(self, bandido_repository : BandidoRepository):
        self.bandido_repository = bandido_repository

    def execute(self, asalto: Asalto) -> float:
        nota_final = 0
        puntos_cantidad = asalto.notas.__len__()
        if puntos_cantidad > 0:
            for nota in asalto.notas:
                nota_final += nota

            nota_final = nota_final / puntos_cantidad
            asalto.sheriff.actualizar_puntos(nota_final)
            self.bandido_repository.update(asalto.sheriff)

        return nota_final
