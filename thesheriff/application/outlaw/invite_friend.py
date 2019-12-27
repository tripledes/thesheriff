import inject
from thesheriff.domain.mail.mail_factory import MailFactory
from thesheriff.domain.mail.notifier.mail_notifier import MailNotifier
from thesheriff.domain.outlaw.outlaw import Outlaw
from typing import NoReturn


class InviteFriend:
    """Class InviteFriend implements the invite a friend use case.

    :param mail_notifier: Notifier object to handle email notifications.
    :type mail_notifier: MailNotifier
    """

    @inject.autoparams()
    def __init__(self, mail_notifier: MailNotifier):
        self.__mail_notifier = mail_notifier

    def execute(self, receiver_mail_address):
        """execute is the actual action of the Invite Friend use case.

        :param receiver_mail_address: The address to write on the TO field.
        :type receiver_mail_address: String
        :return: No value returned.
        :rtype: NoReturn
        """
        sender = Outlaw.get_email()
        receiver = receiver_mail_address
        mail = MailFactory.mail_invite_friend(sender, receiver)
        self.__mail_notifier.send(mail=mail)
