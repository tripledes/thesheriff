from tests.mocks.mock_gang_repository import MockGangRepository
from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.gang.request.join_gang_request \
    import JoinGangRequest
from thesheriff.application.outlaw.join_gang import JoinGang
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw


def test_join_gangs():
    gang_repository = MockGangRepository()
    outlaw_repository = MockOutlawRepository()

    previous_gang = Gang(1, "APreviousGang")
    gang_i_want_to_join = Gang(2, "TheWorstGang")
    gang_repository.add(gang_i_want_to_join)
    outlaw = Outlaw("VeryBadGuy", "iamabadguy@yopmail.com", 1)
    outlaw.gangs = [previous_gang]
    outlaw_repository.add(outlaw)

    request = JoinGangRequest(gang_i_want_to_join.id, outlaw.id)
    JoinGang(outlaw_repository, gang_repository).execute(request)

    assert len(outlaw.gangs) == 2
