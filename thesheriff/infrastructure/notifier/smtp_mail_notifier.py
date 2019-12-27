import smtplib
import ssl

from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.mail.mail_factory import MailFactory
from thesheriff.domain.mail.notifier.mail_notifier import MailNotifier


class SMTPMailNotifier(MailNotifier):

    def __init__(self):
        # Create a secure SSL context
        self.port = 465
        self.context = ssl.create_default_context()
        # TODO(all): read the password from an environment variable
        self.password = "thesheriff123"

    def send(self, mail: Mail):
        with smtplib.SMTP_SSL("smtp.gmail.com",
                              self.port,
                              context=self.context) as server:

            # To send the email, we log into the system with the sender address
            server.login(MailFactory.APPLICATION_MAIL, self.password)
            server.sendmail(mail.sender, mail.receiver, mail.content)
