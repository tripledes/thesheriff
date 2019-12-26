import smtplib
import ssl

from thesheriff.domain.mail.notifier.mail_notifier import MailNotifier


class SMTPMailNotifier(MailNotifier):
    global port  # For SSL
    global context
    global password

    # Create a secure SSL context
    port = 465
    context = ssl.create_default_context()
    # TODO(all): read the password from an environment variable
    password = "thesheriff123"

    def send(self, mail):
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) \
                as server:
            # To send the email, we log into the system with the sender address
            server.login(mail.sender, password)
            server.sendmail(mail.sender, mail.receiver, mail.content)
