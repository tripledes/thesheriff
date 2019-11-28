from thesheriff.application.bandido.puntuar_asalto import PuntuarAsalto
from thesheriff.domain.asalto.asalto import Asalto
from thesheriff.domain.asalto.asalto_repository import AsaltoRepository
from thesheriff.domain.bandido.bandido import Bandido
from thesheriff.domain.bandido.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.puntuacion import Puntuacion


class BandidoRepositoryMock(BandidoRepository):
    def of_id(self, bandido_id):
        return Bandido(None, None)

    def add(self):
        pass

    def update(self, bandido : Bandido):
        pass

    def remove(self):
        pass

class AsaltoRepositoryMock(AsaltoRepository):
    def of_id(self):
        pass

    def add(self):
        pass

    def update(self, asalto: Asalto):
        pass

def test_puntuar_asalto():
    asalto = Asalto(None, None, None, None)
    puntuar_asalto = PuntuarAsalto(asalto, BandidoRepositoryMock(), AsaltoRepositoryMock())

    puntuar_asalto.execute(Bandido(None, None), Puntuacion(5, 6, 7, 5.5))
    puntuar_asalto.execute(Bandido(None, None), Puntuacion(7, 8.5, 8, 9))

    assert 2 == asalto.notas.__len__()
    assert 5.875 == asalto.notas[0]
    assert 8.125 == asalto.notas[1]
