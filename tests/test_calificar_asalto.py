from thesheriff.application.asalto.calificar_asalto import CalificarAsalto
from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.sheriff import Sheriff

class BandidoRepositoryMock(BandidoRepository):
    def of_id(self):
        pass

    def add(self):
        pass

    def update(self, bandido):
        pass

    def remove(self):
        pass

def test_calificar_asalto():
    sheriff = Sheriff(Bandido(1, "el sheriff"))
    sheriff.actualizarPuntos(22)

    asalto = Asalto(1, "restaurante muy bueno", None, sheriff)

    asalto.nuevaPuntuacion(10)
    asalto.nuevaPuntuacion(9)
    asalto.nuevaPuntuacion(7)
    asalto.nuevaPuntuacion(8)

    resultado = CalificarAsalto(asalto, BandidoRepositoryMock()).execute()

    assert 8.5 == resultado
    assert 30.5 == sheriff.puntos
