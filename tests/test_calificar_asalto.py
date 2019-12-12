from tests.bandido_mock_repository import BandidoMockRepository
from thesheriff.application.asalto.calificar_asalto import CalificarAsalto
from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.sheriff import Sheriff


def test_calificar_asalto():
    sheriff = Sheriff(Bandido(1, "el sheriff", "sheriff@yopmail.com"))
    sheriff.actualizar_puntos(22)

    asalto = Asalto(1, "restaurante muy bueno", None, sheriff, None)

    asalto.nueva_puntuacion(10)
    asalto.nueva_puntuacion(9)
    asalto.nueva_puntuacion(7)
    asalto.nueva_puntuacion(8)

    resultado = CalificarAsalto(BandidoMockRepository()).execute(asalto)

    assert 8.5 == resultado
    assert 30.5 == sheriff.puntos
