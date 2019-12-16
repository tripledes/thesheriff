from tests.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.raid.grade_raid import GradeRaid
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff


def test_grade_raid():
    sheriff = Sheriff(Outlaw(1, "the sheriff", "sheriff@yopmail.com"))
    sheriff.update_score(22)

    raid = Raid("very nice restaurant", None, sheriff, None, None)

    raid.add_rate(10)
    raid.add_rate(9)
    raid.add_rate(7)
    raid.add_rate(8)

    result = GradeRaid(MockOutlawRepository()).execute(raid)

    assert 8.5 == result
    assert 30.5 == sheriff.get_score()
