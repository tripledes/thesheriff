import inject
from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.mail.repository.mail_notification \
    import MailNotification
from thesheriff.domain.outlaw.outlaw import Outlaw


class InviteFriend:

    @inject.autoparams()
    def __init__(self, mail_repository: MailNotification):
        self.mail_repository = mail_repository

    def execute(self, receiver_mail_address):
        sender = Outlaw.get_email()
        receiver = receiver_mail_address
        mail = Mail.mail_invite_friend(sender, receiver)
        self.mail_repository.send(mail)
