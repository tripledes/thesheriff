from tests.asalto_mock_repository import AsaltoMockRepository
from tests.bandido_mock_repository import BandidoMockRepository
from thesheriff.application.bandido.puntuar_asalto import PuntuarAsalto
from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.puntuacion import Puntuacion


def test_puntuar_asalto():
    bandido_repository = BandidoMockRepository()
    bandido = Bandido(1, None, None)
    bandido_repository.add(bandido)

    asalto_repository = AsaltoMockRepository()
    asalto = Asalto(1, None, None, None, None)
    asalto_repository.add(asalto)

    puntuar_asalto = PuntuarAsalto(bandido_repository, asalto_repository)
    puntuar_asalto.execute(asalto.id, bandido.id, Puntuacion(5, 6, 7, 5.5))
    puntuar_asalto.execute(asalto.id, bandido.id, Puntuacion(7, 8.5, 8, 9))

    assert 2 == asalto.notas.__len__()
    assert 5.875 == asalto.notas[0]
    assert 8.125 == asalto.notas[1]
