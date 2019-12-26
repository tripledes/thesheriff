from tests.mocks.mock_gang_repository import MockGangRepository
from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from tests.mocks.mock_raid_repository import MockRaidRepository
from thesheriff.application.raid.create_raid import CreateRaid
from thesheriff.application.raid.request.create_raid_request import \
    CreateRaidRequest
from thesheriff.domain.outlaw.outlaw import Outlaw


def test_create_raid():
    name = 'Asalto test'
    date = '2019-12-24 23:59:00'
    location = 'Barcelona'
    gang_id = 1
    sheriff_id = 3
    outlaw_ids = [1, 2, 3]

    request = CreateRaidRequest(
        name, date, location, gang_id, sheriff_id, outlaw_ids)

    outlaw_repository = MockOutlawRepository()
    outlaw_repository.outlaw = Outlaw('Sheriff', 'sheriff@banda.com', 3)

    gang_repository = MockGangRepository()
    gang_repository.gang = gang_repository.all()[0]

    service = CreateRaid(
        outlaw_repository, gang_repository, MockRaidRepository())

    raid = service.execute(request)

    assert raid.name == name
    assert raid.sheriff.id == sheriff_id
