import smtplib
import ssl
from thesheriff.domain.mail.repository.mail_notification \
    import MailNotification


class SMTPMailRepository:
    global port  # For SSL
    global context
    global password

    # Create a secure SSL context
    port = 465
    context = ssl.create_default_context()
    # TODO(all): read the password from an environment variable
    password = "thesheriff123"

    def __init__(self, mail_repository: MailNotification):
        self.mail_repository = mail_repository

    def send(self, mail):
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) \
                as server:
            # To send the email, we log into the system with the sender address
            server.login(mail.sender, password)
            server.sendmail(mail.sender, mail.receiver, mail.content)
