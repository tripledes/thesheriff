from tests.mocks.mock_mail_notifier import MockMailNotifier
from tests.mocks.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.outlaw.invite_friend import InviteFriend
from thesheriff.application.outlaw.request.invite_friend_request import \
    InviteFriendRequest
from thesheriff.domain.outlaw.outlaw import Outlaw


def test_invite_friend():
    notifier = MockMailNotifier()
    outlaw_repository = MockOutlawRepository()

    outlaw = Outlaw("The gang chief", "bad@yopmail.com", 1)
    outlaw_repository.add(outlaw)

    receiver_email = "receiver@yopmail.com"

    invite_friend = InviteFriend(outlaw_repository, notifier)

    request = InviteFriendRequest(outlaw.id, receiver_email)
    mail = invite_friend.execute(request)

    assert mail.sender == outlaw.email
    assert mail.receiver == receiver_email
