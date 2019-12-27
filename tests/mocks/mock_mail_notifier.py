from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.mail.notifier.mail_notifier import MailNotifier


class MockMailNotifier(MailNotifier):

    def send(self, mail: Mail):
        print(mail.content)
