from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.outlaw.create_outlaw import CreateOutlaw
from thesheriff.application.outlaw.request.create_outlaw_request import \
    CreateOutlawRequest


def test_create_outlaw():
    outlaw_repository = MockOutlawRepository()

    request = CreateOutlawRequest("outlaw1", "outlaw1@yopmail.com")

    outlaw = CreateOutlaw(outlaw_repository).execute(request)

    assert outlaw.name == "outlaw1"
    assert outlaw.email == "outlaw1@yopmail.com"
