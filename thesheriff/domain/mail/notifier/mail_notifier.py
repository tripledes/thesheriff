import abc

from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.mail.mail_factory import MailFactory


class MailNotifier(abc.ABC):
    """Interface MailNotifier, defines how all mail notifier
    implementations will behave.
    """

    @abc.abstractmethod
    def send(self, mail: Mail):
        pass
