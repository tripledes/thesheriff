from tests.banda_mock_repository import BandaMockRepository
from thesheriff.application.bandido.listar_bandas import ListarBandas


def test_listar_bandas():
    banda_repository = BandaMockRepository()

    bandas = ListarBandas(banda_repository).execute(1)

    assert len(bandas) == 2
