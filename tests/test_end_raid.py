from tests.mocks.mock_mail_notifier import MockMailNotifier
from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from tests.mocks.mock_raid_repository import MockRaidRepository
from thesheriff.application.raid.end_raid import EndRaid
from thesheriff.application.raid.request.end_raid_request import EndRaidRequest
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff
from thesheriff.domain.raid.raid import Raid


def test_end_raid():
    mail_sender = MockMailNotifier()
    raid_repository = MockRaidRepository()
    outlaw_repository = MockOutlawRepository()

    outlaw_repository.add(Outlaw("1", "email", 1))

    gang = Gang(1, "Gang")
    outlaw1 = Outlaw("2", "email", 2)
    outlaw2 = Outlaw("3", "email", 3)
    outlaws = [outlaw1, outlaw2]
    gang.add_members(outlaws)
    raid = Raid(
        "amazing raid", outlaws, Sheriff("1", "email", 1), gang,
        "street 1, 05", date="2019-12-31 23:59:00"
    )
    raid.rates = list()
    raid.add_rate(10)
    raid.add_rate(9)

    raid_repository.add(raid)

    end_raid = EndRaid(mail_sender, raid_repository, outlaw_repository)
    request = EndRaidRequest(1, 100)
    result = end_raid.execute(request)

    assert result == \
        "Gang's score: 0.0. Sheriff's score on raid 'amazing raid': 100"


def test_raid_can_not_be_ended_throws_exception():
    mail_sender = MockMailNotifier()
    raid_repository = MockRaidRepository()
    outlaw_repository = MockOutlawRepository()

    outlaw_repository.add(Outlaw("1", "email", 1))

    gang = Gang(1, "Gang")
    outlaw1 = Outlaw("2", "email", 2)
    outlaw2 = Outlaw("3", "email", 3)
    outlaws = [outlaw1, outlaw2]
    gang.add_members(outlaws)
    raid = Raid(
        "amazing raid", outlaws, Sheriff("2", "email", 1), gang,
        "street 1, 05", date="2019-12-31 23:59:00"
    )

    raid_repository.add(raid)
    request = EndRaidRequest(1, 100)
    end_raid = EndRaid(mail_sender, raid_repository, outlaw_repository)

    try:
        end_raid.execute(request)
    except Exception as e:
        assert (
            "Raid can not be finished until all outlaws have ranked it."
            == str(e)
        )
