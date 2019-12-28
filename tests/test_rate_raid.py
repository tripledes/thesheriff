from tests.mocks.mock_raid_repository import MockRaidRepository
from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.sheriff import Sheriff
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.score import Score


def test_rate_raid():
    outlaw_repository = MockOutlawRepository()
    outlaw = Outlaw("MockedOutLaw", "iam_a_mocked_outlaw@thesheriff.corp", 1)
    outlaw_repository.add(outlaw)

    gang = Gang(2, "The Gang")
    sheriff = Sheriff("Sheriff", "iam_thesheriff_gang2@thesheriff.corp", 2)

    raid_repository = MockRaidRepository()
    raid = Raid(
        "very nice restaurant", [],
        sheriff, gang, "Barcelona", "2019-12-31 23:59:00"
    )
    raid_repository.add(raid)

    rate_raid = RateRaid(outlaw_repository, raid_repository)
    rate_raid.execute(1, 0, Score(5, 6, 7, 5.5))
    rate_raid.execute(1, 0, Score(7, 8.5, 8, 9))

    assert 2 == len(raid.rates)
    assert 5.875 == raid.rates[0]
    assert 8.125 == raid.rates[1]
