from thesheriff.application.bandido.puntuar_asalto import PuntuarAsalto
from thesheriff.domain.bandido.bandido import Bandido

def test_puntuar_asalto(self):

    puntuar_asalto = PuntuarAsalto(Bandido())

    puntuar_asalto.puntuar(10)
    puntuar_asalto.puntuar(8)
    puntuar_asalto.puntuar(9)
    puntuar_asalto.puntuar(7)
    puntuar_asalto.puntuar(7.5)

    assert puntuar_asalto.execute() == 8.3
