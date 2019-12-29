from tests.mocks.mock_gang_repository import MockGangRepository
from thesheriff.application.outlaw.list_gangs import ListGangs
from thesheriff.application.outlaw.request.list_gangs_request import \
    ListGangsRequest


def test_outlaw_list_gangs():
    gang_repository = MockGangRepository()

    request = ListGangsRequest(outlaw_id=1)
    gangs = ListGangs(gang_repository).execute(request)

    assert len(gangs) == 2
