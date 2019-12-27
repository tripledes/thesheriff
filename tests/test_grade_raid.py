from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from tests.mocks.mock_raid_repository import MockRaidRepository
from thesheriff.application.raid.grade_raid import GradeRaid
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff


def test_grade_raid():
    sheriff = Sheriff("the sheriff", "sheriff@yopmail.com", 1)
    sheriff.update_score(22.0)

    gang = Gang(2, "The Gang")
    raid = Raid(
        "very nice restaurant", [], sheriff,
        gang, "Fake ST 123", "2019-12-31 23:59:00"
    )
    raid.rates = list()
    raid.add_rate(10)
    raid.add_rate(9)
    raid.add_rate(7)
    raid.add_rate(8)

    raid_repository = MockRaidRepository()
    raid_repository.add(raid)

    outlaw_repository = MockOutlawRepository()

    result = GradeRaid(raid_repository, outlaw_repository).execute(1)

    assert 8.5 == result
    assert 30.5 == sheriff.get_score()
