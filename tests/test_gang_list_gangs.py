from tests.mocks.mock_gang_repository import MockGangRepository
from thesheriff.application.gang.list_gangs import ListGangs


def test_gang_list_gangs():
    gang_repository = MockGangRepository()

    gangs = ListGangs(gang_repository).execute()

    assert len(gangs) == 3
