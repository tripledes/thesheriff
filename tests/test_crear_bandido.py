from tests.bandido_mock_repository import BandidoMockRepository
from thesheriff.application.bandido.crear_bandido import CrearBandido
from thesheriff.application.bandido.request.crear_bandido_request import CrearBandidoRequest


def test_crear_bandido():
    bandido_repository = BandidoMockRepository()

    request = CrearBandidoRequest("bandido1", "bandido1@yopmail.com")

    bandido = CrearBandido(bandido_repository).execute(request)

    assert bandido.name == "bandido1"
    assert bandido.correo == "bandido1@yopmail.com"
