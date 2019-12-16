from tests.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.outlaw.list_friends import ListFriends


def test_list_friends():
    outlaw_repository = MockOutlawRepository()

    friends = ListFriends(outlaw_repository).execute(1)

    assert len(friends) == 3
