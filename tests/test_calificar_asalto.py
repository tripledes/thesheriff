from tests.bandido_mock_repository import BandidoMockRepository
from thesheriff.application.asalto.calificar_asalto import CalificarAsalto
from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.sheriff import Sheriff

def test_calificar_asalto():
    sheriff = Sheriff(Bandido(1, "el sheriff", "sheriff@yopmail.com"))
    sheriff.actualizarPuntos(22)

    asalto = Asalto(1, "restaurante muy bueno", None, sheriff)

    asalto.nuevaPuntuacion(10)
    asalto.nuevaPuntuacion(9)
    asalto.nuevaPuntuacion(7)
    asalto.nuevaPuntuacion(8)

    resultado = CalificarAsalto(asalto, BandidoMockRepository()).execute()

    assert 8.5 == resultado
    assert 30.5 == sheriff.puntos
