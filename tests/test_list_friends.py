from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.outlaw.list_friends import ListFriends
from thesheriff.application.outlaw.request.list_friends_request import \
    ListFriendsRequest


def test_list_friends():
    outlaw_repository = MockOutlawRepository()

    request = ListFriendsRequest(outlaw_id=1)
    friends = ListFriends(outlaw_repository).execute(request)

    assert len(friends) == 3
