from tests.bandido_mock_repository import BandidoMockRepository
from thesheriff.application.bandido.listar_amigos import ListarAmigos


def test_listar_amigos():
    bandido_repository = BandidoMockRepository()

    amigos = ListarAmigos(bandido_repository).execute(1)

    assert len(amigos) == 3
