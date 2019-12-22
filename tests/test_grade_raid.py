from datetime import datetime

from tests.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.raid.grade_raid import GradeRaid
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff


def test_grade_raid():
    sheriff = Sheriff(Outlaw(1, "the sheriff", "sheriff@yopmail.com"))
    sheriff.update_score(22)

    gang = Gang(2, "The Gang")

    raid = Raid("very nice restaurant", "Fake ST 123", sheriff, gang, datetime.now(), None)

    raid.add_rate(10)
    raid.add_rate(9)
    raid.add_rate(7)
    raid.add_rate(8)

    result = GradeRaid(MockOutlawRepository()).execute(raid)

    assert 8.5 == result
    assert 30.5 == sheriff.get_score()
