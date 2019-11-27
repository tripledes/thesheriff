from thesheriff.application.bandido.puntuar_asalto import PuntuarAsalto
from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.puntuacion import Puntuacion


class BandidoRepositoryMock(BandidoRepository):
    def of_id(self, bandido_id):
        return Bandido(None, None)

    def add(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass


def test_puntuar_asalto():
    asalto = Asalto(None, None, None, None)
    puntuar_asalto = PuntuarAsalto(asalto, BandidoRepositoryMock())

    puntuar_asalto.execute(Bandido(None, None), Puntuacion(5, 6, 7, 5.5))
    puntuar_asalto.execute(Bandido(None, None), Puntuacion(7, 8.5, 8, 9))

    assert 2 == asalto.scores.__len__()
    assert 5.875 == asalto.scores[0]
    assert 8.125 == asalto.scores[1]
