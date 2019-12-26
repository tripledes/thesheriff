from tests.mocks.mock_gang_repository import MockGangRepository
from thesheriff.application.gang.request.create_gang_request import \
    CreateGangRequest
from thesheriff.application.outlaw.create_gang import CreateGang


def test_create_gang():
    gang_repository = MockGangRepository()

    request = CreateGangRequest(1, "super gang")

    gang = CreateGang(gang_repository).execute(request)

    assert gang.owner_id == 1
    assert gang.name == "super gang"
