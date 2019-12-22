from datetime import datetime

from tests.mock_raid_repository import MockRaidRepository
from thesheriff.application.raid.end_raid import EndRaid
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from thesheriff.domain.raid.raid import Raid


def test_end_raid():
    raid_repository = MockRaidRepository()
    gang = Gang(1, "Gang")
    outlaw1 = Outlaw(1, "2", "email")
    outlaw2 = Outlaw(2, "3", "email")
    outlaws = [outlaw1, outlaw2]
    gang.add_members(outlaws)
    raid = Raid("amazing raid", "street 1, 05", Sheriff(outlaw1), gang,
                date=datetime.now(), raid_id=None)

    raid.join(outlaw=outlaw1)
    raid.join(outlaw=outlaw2)

    raid.add_rate(10)
    raid.add_rate(9)

    raid_repository.add(raid)

    end_raid = EndRaid(raid_repository)

    result = end_raid.execute(1, 100)

    assert result == "Gang's score: 0. Sheriff's score on raid 'amazing raid': 100"


def test_raid_can_not_be_ended_throws_exception():
    raid_repository = MockRaidRepository()
    gang = Gang(1, "Gang")
    outlaw1 = Outlaw(1, "2", "email")
    outlaw2 = Outlaw(2, "3", "email")
    outlaws = [outlaw1, outlaw2]
    gang.add_members(outlaws)
    raid = Raid("amazing raid", "street 1, 05", Sheriff(outlaw1), gang,
                date=datetime.now(), raid_id=None)

    raid.join(outlaw=outlaw1)
    raid.join(outlaw=outlaw2)

    raid.add_rate(10)

    raid_repository.add(raid)

    end_raid = EndRaid(raid_repository)

    try:
        end_raid.execute(1, 100)
    except Exception as e:
        assert ("Raid can not be finished until all outlaws have ranked it." == str(e))
