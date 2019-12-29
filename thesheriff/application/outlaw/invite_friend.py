import inject

from thesheriff.application.outlaw.request.invite_friend_request import \
    InviteFriendRequest
from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.mail.mail_factory import MailFactory
from thesheriff.domain.mail.notifier.mail_notifier import MailNotifier
from thesheriff.domain.outlaw.outlaw import Outlaw
from typing import NoReturn

from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository


class InviteFriend:
    """Class InviteFriend implements the invite a friend use case.

    :param outlaw_repository: Associated repo to retrieve outlaw by his id.
    :type outlaw_repository: OutLawRepository
    :param mail_notifier: Notifier object to handle email notifications.
    :type mail_notifier: MailNotifier
    """

    @inject.autoparams()
    def __init__(self, outlaw_repository: OutlawRepository,
                 mail_notifier: MailNotifier):
        self.__outlaw_repository = outlaw_repository
        self.__mail_notifier = mail_notifier

    def execute(self, request: InviteFriendRequest) -> Mail:
        """execute is the actual action of the Invite Friend use case.

        :param request: The address to write on the TO field.
        :type request: InviteFriendRequest
        :return mail: Mail.
        :rtype: Mail
        """
        sender_mail = self.__outlaw_repository.of_id(request.outlaw_id).email
        receiver_mail = request.mail_address_receiver
        mail = MailFactory.mail_invite_friend(sender_mail, receiver_mail)
        self.__mail_notifier.send(mail)
        return mail
