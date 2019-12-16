from tests.mock_gang_repository import MockGangRepository
from thesheriff.application.outlaw.list_gangs import ListGangs


def test_list_gangs():
    gang_repository = MockGangRepository()

    gangs = ListGangs(gang_repository).execute(1)

    assert len(gangs) == 2
