from tests.mocks.mock_raid_repository import MockRaidRepository
from thesheriff.application.raid.end_raid import EndRaid
from thesheriff.application.raid.request.end_raid_request import EndRaidRequest
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from thesheriff.domain.raid.raid import Raid


def test_end_raid():
    raid_repository = MockRaidRepository()
    gang = Gang(1, "Gang")
    outlaw1 = Outlaw("2", "email", 1)
    outlaw2 = Outlaw("3", "email", 2)
    outlaws = [outlaw1, outlaw2]
    gang.add_members(outlaws)
    raid = Raid(
        "amazing raid", outlaws, Sheriff("2", "email", 1), gang,
        "street 1, 05", date="2019-12-31 23:59:00"
    )
    raid.rates = list()
    raid.add_rate(10)
    raid.add_rate(9)

    raid_repository.add(raid)

    end_raid = EndRaid(raid_repository)
    request = EndRaidRequest(1, 100)
    result = end_raid.execute(request)

    assert result == \
        "Gang's score: 0.0. Sheriff's score on raid 'amazing raid': 100"


def test_raid_can_not_be_ended_throws_exception():
    raid_repository = MockRaidRepository()
    gang = Gang(1, "Gang")
    outlaw1 = Outlaw("2", "email", 1)
    outlaw2 = Outlaw("3", "email", 2)
    outlaws = [outlaw1, outlaw2]
    gang.add_members(outlaws)
    raid = Raid(
        "amazing raid", outlaws, Sheriff("2", "email", 1), gang,
        "street 1, 05", date="2019-12-31 23:59:00"
    )

    raid.join(outlaw=outlaw1)
    raid.join(outlaw=outlaw2)
    raid.rates = list()
    raid.add_rate(10)

    raid_repository.add(raid)
    request = EndRaidRequest(1, 100)
    end_raid = EndRaid(raid_repository)

    try:
        end_raid.execute(request)
    except Exception as e:
        assert (
            "Raid can not be finished until all outlaws have ranked it."
            == str(e)
        )
