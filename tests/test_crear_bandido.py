from tests.bandido_mock_repository import BandidoMockRepository
from thesheriff.application.bandido.crear_bandido import CrearBandido


def test_crear_bandido():
    bandido_repository = BandidoMockRepository()

    bandido = CrearBandido(bandido_repository).execute("bandido1", "bandido1@yopmail.com")

    assert bandido.name == "bandido1"
    assert bandido.correo == "bandido1@yopmail.com"
